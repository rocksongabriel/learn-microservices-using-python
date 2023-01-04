from fastapi import FastAPI

from .api.movies import movies

app = FastAPI()

app.include_router(movies, tags=["Movies"])
