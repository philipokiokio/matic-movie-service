from src.comments.models import FilmComment
from sqlalchemy.orm import Session
from typing import Union


# COMMENT ORM
class CommentRepo:
    def __init__(self, db: Session) -> None:
        self.db = db

    # PARTIAL QUERY
    def base(self):
        return self.db.query(FilmComment)

    # CREATE A COMMENT
    def create(self, data: dict):
        comment = FilmComment(**data)
        self.db.add(comment)
        self.db.commit()
        self.db.refresh(comment)
        return comment

    # UPDATE A COMMENT
    def update(self, comment: FilmComment):
        self.db.commit()
        self.db.refresh(comment)
        return comment

    # DELETE COMMENT
    def delete(self, comment: FilmComment):
        self.db.delete(comment)
        self.db.commit()

    # ALL COMMENTS WITH ORDER BY
    def all(self, film_id: int, asc_sort: Union[bool, None]):
        sort_order = []

        if type(asc_sort) == bool:
            if asc_sort:
                sort_order.append(FilmComment.date_created.asc())

            else:
                sort_order.append(FilmComment.date_created.desc())

        return (
            self.base()
            .filter(FilmComment.film_id == film_id)
            .order_by(*sort_order)
            .all()
        )

    # GET BY ID
    def by_id(self, film_id: int, id: int):
        return (
            self.base()
            .filter(FilmComment.id == id, FilmComment.film_id == film_id)
            .first()
        )


# COMMENT REPO INTIALIZATION
comment_repo = CommentRepo
