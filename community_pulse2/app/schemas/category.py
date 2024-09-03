from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str

class CategoryResponse(CategoryCreate):
    id: int
