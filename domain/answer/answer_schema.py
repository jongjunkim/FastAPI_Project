import datetime
from pydantic import BaseModel, field_validator
from domain.user.user_schema import User

class AnswerCreate(BaseModel):
    content: str

    @field_validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Null value is not allowed')
        return v

class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime
    user: User | None