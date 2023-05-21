from fastapi import FastAPI, status, Depends
from src.films.starwars_service import sw_films
from src.films.film_repo import film_repo
from src.app.utils.database_utils import get_db
from sqlalchemy.orm import Session
from src.films.film_router import film_router
from src.comments.comment_router import comment_router

app = FastAPI()


app.include_router(film_router)
app.include_router(comment_router)


@app.get("/", status_code=status.HTTP_200_OK)
async def root(db: Session = Depends(get_db)):
    film_data = await sw_films.flims_data()
    repo = film_repo(db)
    if not repo.all():
        if type(film_data) == list:
            repo.bulk_create(film_data)

    return {
        "message": "Codematic Movie-API take home",
        "docs": "/docs",
        "redoc": "/redocs",
    }
