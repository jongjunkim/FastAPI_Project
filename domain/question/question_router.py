from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models import Question
from database import get_db
from domain.question import question_schema, question_crud

router = APIRouter(
    prefix="/api/question",
)

# @router.get("/list")
# def question_list():
#     with get_db() as db:
#         _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#     return _question_list

#there is more simpler way than using with
#Use Depends

@router.get("/list", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = question_crud.get_question_list(db)
    return _question_list

@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    return question