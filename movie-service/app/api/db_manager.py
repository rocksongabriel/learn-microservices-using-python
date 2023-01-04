from .models import MovieOut, MovieIn, MovieUpdate
from .db import movies, database


async def get_all_movies():
    query = movies.select()

    return await database.fetch_all(query=query)
