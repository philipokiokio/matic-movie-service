from src.comments.comment_repo import comment_repo, FilmComment
from src.comments import schemas
from src.films.film_repo import film_repo, Film
from fastapi import status, HTTPException
from typing import Union


class CommentService:
    # INITIALIZATION
    def __init__(self, db) -> None:
        self.repo = comment_repo(db)
        self.film_repo = film_repo(db)

    # DATA MANIPULATION FOR ORM CALL {LAZY LOADING}
    def orm_call(self, comment: FilmComment):
        comment_dict = comment.__dict__
        comment_dict["film"] = comment.film
        return comment_dict

    # CHECK IF FILM EXISTS
    def film_check(self, film_id: int) -> Film:
        film = self.film_repo.by_id(film_id)
        if film is None:
            raise HTTPException(
                detail="there is no film with this id",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        return film

    # CREATE COMMENT FOR A FILM
    def create(self, film_id: int, comment_create: schemas.CommentCreate):
        film = self.film_check(film_id)

        comment_create = comment_create.dict()
        comment_create["film_id"] = film.id
        comment = self.repo.create(comment_create)
        return {
            "message": "comment created successfully",
            "data": self.orm_call(comment),
            "status": status.HTTP_201_CREATED,
        }

    # GET ALL COMMENTS FOR A FILE
    def get_comments(
        self, film_id: int, asc_sort: Union[bool, None] = None
    ) -> schemas.MessageListCommentResponse:
        film = self.film_check(film_id)

        comments = self.repo.all(film.id, asc_sort)
        if not comments:
            raise HTTPException(
                detail="there are no comments for this film",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        comments_ = [self.orm_call(comment) for comment in comments]
        return {
            "message": "comments retrieved successfully",
            "data": comments_,
            "status": status.HTTP_200_OK,
        }

    # GET A COMMENT BASED ON FILM ID AND COMMENT ID
    def get_comment(
        self, film_id: int, comment_id: int
    ) -> schemas.MessageCommentReponse:
        film = self.film_check(film_id)
        comment = self.repo.by_id(film.id, comment_id)
        if not comment:
            raise HTTPException(
                detail="there is no comment for this film with this id",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        return {
            "message": "comment retrieved successfully",
            "data": self.orm_call(comment),
            "status": status.HTTP_200_OK,
        }

    # UPDATE A COMMENT TEXT
    def update_comment(
        self, film_id: int, comment_id: int, comment_update: schemas.CommentCreate
    ) -> schemas.MessageCommentReponse:
        film = self.film_check(film_id)
        comment = self.repo.by_id(film.id, comment_id)
        if not comment:
            raise HTTPException(
                detail="there is no comment for this film with this id",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        for key, value in comment_update.dict().items():
            setattr(comment, key, value)

        comment = self.repo.update(comment)
        return {
            "message": "comment updated successfully",
            "data": self.orm_call(comment),
            "status": status.HTTP_200_OK,
        }

    # DELETE COMMENT
    def delete_comment(self, film_id: int, comment_id: int):
        film = self.film_check(film_id)
        comment = self.repo.by_id(film.id, comment_id)
        if not comment:
            raise HTTPException(
                detail="there is no comment for this film with this id",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        self.repo.delete(comment)
        return {"status": status.HTTP_204_NO_CONTENT}


# INTIALIZING SERVICE
comment_service = CommentService
