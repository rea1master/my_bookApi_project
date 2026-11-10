from typing import Optional
from model import BookCreate,BookUpdate
from datetime import date

books_db:dict[int,dict]={}
next_id=int(1)

def create_book(book:BookCreate) ->dict:
    """创建图书"""
    global next_id
    book_dict=book.model_dump()
    # 增加为字符串变量id的key,让key的值是int的next_id
    book_dict["id"]=next_id  
    books_db[next_id]=book_dict
    next_id+=1
    return book_dict

def get_book(book_id:int)->dict:
    """获取图书"""
    if(book_id not in books_db) :return None
    return books_db.get(book_id)

def get_books(skip:int =0,limit:int =10)->tuple[list[dict],int]:
    """获取图书列表"""
    all_books=list(books_db.values())
    total=len(all_books)
    books = all_books[skip: skip+limit]
    return books,total

def update_book(book_id:int,book:BookUpdate)->dict:
    """更新图书"""
    if(book_id not in books_db):return None
    update_date=book.model_dump(exclude_unset=True)
    books_db[book_id].update(update_date)
    return books_db[book_id]

def delete_book(book_id)->bool:
    """删除图书"""
    if(book_id not in books_db): return False
    else: 
        del books_db[book_id] 
        return True



# 创建样例
def sample_book():
    books=[
        BookCreate(
            title="肖生客的救赎",
            author= "Morgen",
            isbn="1111111111111",
            price=41.9,
            published_date=date(2002,10,27),
            description="救赎之道,就在其中",
        ),
        BookCreate(
            title="高等数学",
            author= "刘晓燕",
            isbn="2222222222222",
            price= 29.9,
            published_date=date(2008,5,1),
            description="救赎之道,就在其中",
        )
    ]
    for i in books:
        create_book(i)

sample_book()