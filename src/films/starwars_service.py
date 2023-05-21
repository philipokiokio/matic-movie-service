from src.app.utils.config import sw_settings
from httpx import AsyncClient


class StarWarsFilms:
    def __init__(self) -> None:
        self.client = AsyncClient()

    # FETCH STAR WARS FILMS
    async def flims_data(self):
        film_data = await self.client.get(f"{sw_settings.base_url}films/")
        if film_data.status_code >= 400:
            return {"detail": "no data issue with integration"}
        data = film_data.json()
        return data.get("results")


sw_films = StarWarsFilms()
