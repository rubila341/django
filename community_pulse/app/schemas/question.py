from pydantic import BaseModel

class QuestionCreate(BaseModel):
    title: str
    description: str

class QuestionResponse(QuestionCreate):
    id: int
