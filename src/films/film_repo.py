from src.films.models import Film
from sqlalchemy.orm import Session
from typing import Union, List
from src.films.schemas import FilmCreate


# FILM ORM
class FilmRepo:
    def __init__(self, db: Session):
        self.db = db

    # PARTIAL QUERY
    def base(self):
        return self.db.query(Film)

    # ALL FILMS WITH A ORDER BY
    def all(self, asc_sort: Union[bool, None] = None):
        sort_order = []

        if type(asc_sort) == bool:
            if asc_sort:
                sort_order.append(Film.release_date.asc())

            else:
                sort_order.append(Film.release_date.desc())

        return self.base().order_by(*sort_order).all()

    # GET BY ID
    def by_id(self, id: int):
        return self.base().filter(Film.id == id).first()

    # CREATE A FILM
    def create(self, data: dict):
        film = Film(**data)
        self.db.add(film)
        self.db.commit()
        self.db.refresh(film)
        return film

    # CREATE BULK FILM
    def bulk_create(self, data: List[dict]):
        data = [
            FilmCreate(title=data_["title"], release_date=data_["release_date"]).dict()
            for data_ in data
        ]

        def create_film_obj(data: dict):
            return Film(**data)

        films = list(map(create_film_obj, data))
        self.db.add_all(films)
        self.db.commit()

    # UPDATE FILM
    def update(self, film: Film):
        self.db.commit()
        self.db.refresh(film)
        return film

    # DELETE FIM
    def delete(self, film: Film):
        # CASCADE DELETE FOR RELATIONSHIPS
        if film.comment:
            for comment in film.comment:
                self.db.delete(comment)

        self.db.delete(film)
        self.db.commit()


# FILM_REPO INITIALIZATION
film_repo = FilmRepo
