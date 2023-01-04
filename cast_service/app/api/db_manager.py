from .db import database, casts
from .models import CastIn


async def add_cast(payload: CastIn):
    query = casts.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_cast(id: int):
    query = casts.select().where(casts.c.id == id)

    return await database.fetch_one(query=query)


async def all_casts():
    query = casts.select()

    return await database.fetch_all(query=query)
