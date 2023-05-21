from src.app.utils.schema_utils import ResponseModel, AbstractModel
from datetime import date, datetime
from typing import List, Optional


class FilmCreate(AbstractModel):
    title: str
    release_date: date


class FilmResponse(FilmCreate):
    id: int
    comment_count: int
    date_created: datetime


class MessageListFilmResponse(ResponseModel):
    data: List[FilmResponse]


class MessageFilmResponse(ResponseModel):
    data: FilmResponse


class FlimUpdate(AbstractModel):
    title: Optional[str]
    release_date: Optional[date]
