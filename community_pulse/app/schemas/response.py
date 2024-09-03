from pydantic import BaseModel

class ResponseCreate(BaseModel):
    question_id: int
    text: str

class ResponseResponse(ResponseCreate):
    id: int
