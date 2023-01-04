from .models import MovieOut, MovieIn, MovieUpdate
from .db import movies, database


async def get_all_movies():
    query = movies.select()

    return await database.fetch_all(query=query)


async def add_movie(payload: MovieIn):
    query = movies.insert().values(**payload.dict())

    return await database.execute(query=query)
