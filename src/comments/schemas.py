from src.app.utils.schema_utils import ResponseModel, AbstractModel
from pydantic import constr
from datetime import date, datetime
from typing import List


class CommentCreate(AbstractModel):
    text: constr(max_length=500)


class Film(AbstractModel):
    id: int
    title: str
    release_date: date


class CommentResponse(CommentCreate):
    id: int
    film: Film
    date_created: datetime


class MessageCommentReponse(ResponseModel):
    data: CommentResponse


class MessageListCommentResponse(ResponseModel):
    data: List[CommentResponse]
