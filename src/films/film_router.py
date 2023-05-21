from fastapi import APIRouter, status, Depends
from src.app.utils.database_utils import get_db
from src.films import schemas
from sqlalchemy.orm import Session
from src.films.film_service import film_service
from typing import Union

film_router = APIRouter(
    prefix="/api/v1/film",
    tags=["Film Endpoint Collections {CREATE, SINGLETON, COLLECTION, UPDATE, DESTROY}"],
)


@film_router.post(
    "/create/",
    name="Create Film",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.MessageFilmResponse,
)
def create_film(create_film: schemas.FilmCreate, db: Session = Depends(get_db)):
    return film_service(db).create_film(create_film)


@film_router.get(
    "s/",
    name="Film Collection",
    status_code=status.HTTP_200_OK,
    response_model=schemas.MessageListFilmResponse,
)
def get_films(asc_sort: Union[bool, None] = None, db: Session = Depends(get_db)):
    return film_service(db).get_films(asc_sort)


@film_router.get(
    "/{film_id}/",
    name="Film Signleton",
    status_code=status.HTTP_200_OK,
    response_model=schemas.MessageFilmResponse,
)
def get_film(film_id: int, db: Session = Depends(get_db)):
    return film_service(db).get_film(film_id)


@film_router.patch(
    "/{film_id}/update/",
    name="Film Update",
    status_code=status.HTTP_200_OK,
    response_model=schemas.MessageFilmResponse,
)
def update_film(
    film_id: int, film_update: schemas.FlimUpdate, db: Session = Depends(get_db)
):
    return film_service(db).update_film(film_id, film_update)


@film_router.delete(
    "/{film_id}/delete/", status_code=status.HTTP_204_NO_CONTENT, name="Delete Film"
)
def delete_film(film_id: int, db: Session = Depends(get_db)):
    return film_service(db).delete_film(film_id)
