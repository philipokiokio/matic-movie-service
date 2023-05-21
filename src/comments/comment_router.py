from fastapi import APIRouter, status, Depends
from src.app.utils.database_utils import get_db
from sqlalchemy.orm import Session
from src.comments import schemas
from src.comments.comment_service import comment_service
from typing import Union


comment_router = APIRouter(
    prefix="/api/v1/comment",
    tags=[
        "Flim Comment Enpoint Collections {CREATE, SINGLETON, COLLECTION, UPDATE, DESTROY}"
    ],
)


@comment_router.post(
    "/film/{film_id}/create/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.MessageCommentReponse,
    name="Create Comment",
)
def create_comment(
    film_id: int, comment_create: schemas.CommentCreate, db: Session = Depends(get_db)
):
    return comment_service(db).create(film_id, comment_create)


@comment_router.get(
    "s/film/{film_id}/",
    name="Comment Collection",
    status_code=status.HTTP_200_OK,
    response_model=schemas.MessageListCommentResponse,
)
def get_comments(
    film_id: int, asc_sort: Union[bool, None] = None, db: Session = Depends(get_db)
):
    return comment_service(db).get_comments(film_id, asc_sort)


@comment_router.get(
    "/{comment_id}/film/{film_id}/",
    name="Comment Singleton",
    status_code=status.HTTP_200_OK,
    response_model=schemas.MessageCommentReponse,
)
def get_comment(comment_id: int, film_id: int, db: Session = Depends(get_db)):
    return comment_service(db).get_comment(film_id, comment_id)


@comment_router.patch(
    "/{comment_id}/film/{film_id}/update/",
    status_code=status.HTTP_200_OK,
    name="Update Comment",
    response_model=schemas.MessageCommentReponse,
)
def update_comment(
    comment_id: int,
    film_id: int,
    comment_update: schemas.CommentCreate,
    db: Session = Depends(get_db),
):
    return comment_service(db).update_comment(film_id, comment_id, comment_update)


@comment_router.delete(
    "/{comment_id}/film/{film_id}/delete/",
    status_code=status.HTTP_204_NO_CONTENT,
    name="Delete comment",
)
def delete_comment(
    comment_id: int,
    film_id: int,
    db: Session = Depends(get_db),
):
    return comment_service(db).delete_comment(film_id, comment_id)
