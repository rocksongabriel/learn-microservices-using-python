from fastapi import FastAPI, HTTPException, status, Header, APIRouter

from .models import MovieIn, MovieOut, MovieUpdate
from . import db_manager

movies = APIRouter()


@movies.get("/", response_model=list[MovieOut])
async def all_movies():
    return await db_manager.get_all_movies()


@movies.get("/{id}", response_model=MovieOut)
async def movie(id: int):
    return await db_manager.get_movie(id)


@movies.post("/", status_code=status.HTTP_201_CREATED)
async def add_movie(payload: MovieIn):
    movie_id = await db_manager.add_movie(payload)
    response = {"id": movie_id, **payload.dict()}

    return response


@movies.put("/{id}/")
async def update_movie(id: int, payload: MovieUpdate):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movie with given id not found",
        )

    update_data = payload.dict(exclude_unset=True)
    movie_in_db = MovieUpdate(**movie)

    updated_movie = movie_in_db.copy(update=update_data)

    return await db_manager.update_movie(id, updated_movie)


@movies.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movie with given id not found",
        )

    return await db_manager.delete_movie(id)
