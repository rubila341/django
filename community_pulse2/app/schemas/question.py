from pydantic import BaseModel
from typing import List, Optional

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class QuestionCreate(BaseModel):
    title: str
    description: str
    category_id: int  # Добавлено

class QuestionResponse(QuestionCreate):
    id: int
    category: Optional[CategoryResponse]  # Добавлено

    class Config:
        orm_mode = True
