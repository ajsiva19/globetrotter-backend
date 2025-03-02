from pydantic import BaseModel

class AnswerRequest(BaseModel):
    city: int
    answer: str
