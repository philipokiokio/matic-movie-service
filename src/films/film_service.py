from src.films.film_repo import film_repo, Film
from src.films import schemas
from fastapi import HTTPException, status
from typing import Union


class FilmService:
    # INITLALIZING REPO
    def __init__(self, db) -> None:
        self.repo = film_repo(db)

    # DATA MANIPULATION OF DATA
    def orm_call(self, film: Film):
        film_dict = film.__dict__
        film_dict["comment_count"] = len(film.comment)
        film_dict["comments"] = film.comment
        return film_dict

    # CREATE A FILM
    def create_film(
        self, film_create: schemas.FilmCreate
    ) -> schemas.MessageFilmResponse:
        film = self.repo.create(film_create.dict())

        return {
            "message": "film created successfully",
            "data": self.orm_call(film),
            "status": status.HTTP_201_CREATED,
        }

    # GET A FILMS
    def get_films(
        self, asc_sort: Union[bool, None] = None
    ) -> schemas.MessageListFilmResponse:
        films = self.repo.all(asc_sort)
        if not films:
            raise HTTPException(
                detail="there are no films in the service",
                status_code=status.HTTP_404_NOT_FOUND,
            )

        data = [self.orm_call(film) for film in films]
        return {
            "message": "films retrieved successfully",
            "data": data,
            "status": status.HTTP_200_OK,
        }

    # GET A FILM
    def get_film(self, _id: int) -> schemas.MessageFilmResponse:
        film = self.repo.by_id(_id)
        if film is None:
            raise HTTPException(
                detail="there is no film with this id",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        return {
            "message": "film retrieved successfully",
            "data": self.orm_call(film),
            "status": status.HTTP_200_OK,
        }

    # UPDATE A FILM
    def update_film(
        self, _id: int, film_update: schemas.FlimUpdate
    ) -> schemas.MessageFilmResponse:
        film = self.repo.by_id(_id)
        if film is None:
            raise HTTPException(
                detail="there is no film with this id",
                status_code=status.HTTP_404_NOT_FOUND,
            )

        film_dict = film_update.dict(exclude_unset=True)
        for key, value in film_dict.items():
            setattr(film, key, value)
        film = self.repo.update(film)

        return {
            "message": "film updated successfully",
            "data": self.orm_call(film),
            "status": status.HTTP_200_OK,
        }

    # DELETE A FILM
    def delete_film(self, _id: int):
        film = self.repo.by_id(_id)
        if film is None:
            raise HTTPException(
                detail="there is no film with this id",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        film = self.repo.delete(film)

        return {
            "status": status.HTTP_204_NO_CONTENT,
        }


# INITALIZING SERIVCE
film_service = FilmService
