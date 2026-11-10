from pydantic import Field,field_validator,BaseModel
from datetime import date
from typing import Optional

class BookBase(BaseModel):
    """基础模型"""
    title: str = Field(..., min_length=1, max_length=200, description="书名")
    author: str = Field(..., min_length=1, max_length=100, description="作者")
    isbn: str = Field(..., pattern=r'^\d{13}$', description="ISBN(13位数字)")
    price: float = Field(..., gt=0, description="价格(必须大于0)")
    published_date: date = Field(..., description="出版日期")
    description: Optional[str] = Field(None, max_length=1000, description="图书描述")

class BookCreate(BookBase):
    """创建书"""
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200, description="书名")
    author: Optional[str] = Field(None, min_length=1, max_length=100, description="作者")
    isbn: Optional[str] = Field(None, pattern=r'^\d{13}$', description="ISBN(13位数字)")
    price: Optional[float] = Field(None, gt=0, description="价格(必须大于0)")
    published_date: Optional[date] = Field(None, description="出版日期")
    description: Optional[str] = Field(None, max_length=1000, description="图书描述")

class BookResponse(BookBase):
    id:int
    class Config:
        from_attributes=True

class BooksResponse(BaseModel):
    total: int = Field(..., description="总数")
    page: int = Field(..., description="当前页")
    page_size: int = Field(..., description="每页数量")
    books:list[BookResponse]=Field(...,description="书")

class MessageResponse(BaseModel):
    message:str