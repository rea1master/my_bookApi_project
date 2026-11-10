from fastapi import FastAPI,HTTPException,Query
from model import BookCreate,BookUpdate,BookResponse,BooksResponse,MessageResponse
import datebase as db

app=FastAPI()

@app.get("/",response_model=MessageResponse)
def get_in_8000():
    return {"message":"访问/docs进行更多操作"}

# 创建图书
@app.post("/books",response_model=BookResponse)
def main_create_book(book:BookCreate):
    new_book=db.create_book(book)
    return BookResponse(**new_book)

# 更新图书
@app.put("/books/{book_id}",response_model=BookResponse)
def main_update_book(book_id:int,book:BookUpdate):
    updated_book=db.update_book(book_id,book)
    if updated_book is None:
        raise HTTPException(status_code=404,detail="输入书本id错误")
    else : return BookResponse(**updated_book)


# 获取图书
@app.get("/books/{book_id}",response_model=BookResponse)
def main_get_book(book_id:int):
    geted_book=db.get_book(book_id)
    if(geted_book is None) :raise HTTPException(status_code=404,detail="输入书本id错误")
    else: return BookResponse(**geted_book)

# 获取图书列表 
@app.get("/books/",response_model=BooksResponse)
def main_get_books(
    # Query是查询参数,(默认值，规则，描述)
    page:int = Query(1, ge=1, description="页码"),
    page_size:int = Query(10, ge=1, le=100, description="每页数量")
):
    #page是页码数，page_size是每页大小
    skip=(page-1)*page_size
    books,total=db.get_books(skip=skip,limit=page_size)
    return BooksResponse(
        total=total,
        page=page,
        page_size=page_size,
        books=[BookResponse(**book) for book in books]
    )
    
    
#删除图书
@app.delete("/books/{book_id}",response_model=MessageResponse)
def main_delete_book(book_id:int):
    if(db.delete_book(book_id)): return MessageResponse(message="删除成功")
    else : raise HTTPException(status_code=404,detail="输入书本id错误")