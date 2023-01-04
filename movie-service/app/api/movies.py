from fastapi import FastAPI, HTTPException, status, Header, APIRouter

from .models import MovieIn, MovieOut, MovieUpdate
from . import db_manager

movies = APIRouter(prefix="/movies")

fake_movie_db = [
    {
        "name": "Star Wars: Episode IX - The Rise of Skywalker",
        "plot": "The surviving members of the resistance face the First Order once again.",
        "genres": ["Action", "Adventure", "Fantasy"],
        "casts": ["Daisy Ridley", "Adam Driver"],
    },
    {
        "name": "The Shawshank Redemption",
        "plot": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "genres": ["Drama"],
        "casts": ["Tim Robbins", "Morgan Freeman"],
    },
    {
        "name": "The Dark Knight",
        "plot": "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham. The Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
        "genres": ["Action", "Crime", "Drama"],
        "casts": ["Christian Bale", "Heath Ledger"],
    },
    {
        "name": "Inception",
        "plot": "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
        "genres": ["Action", "Adventure", "Sci-Fi"],
        "casts": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
    },
    {
        "name": "The Godfather",
        "plot": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        "genres": ["Crime", "Drama"],
        "casts": ["Marlon Brando", "Al Pacino"],
    },
    {
        "name": "The Godfather: Part II",
        "plot": "The early life and career of Vito Corleone in 1920s New York is portrayed while his son, Michael, expands and tightens his grip on the family crime syndicate.",
        "genres": ["Crime", "Drama"],
        "casts": ["Robert De Niro", "Al Pacino"],
    },
    {
        "name": "The Matrix",
        "plot": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
        "genres": ["Action", "Sci-Fi"],
        "casts": ["Keanu Reeves", "Laurence Fishburne"],
    },
    {
        "name": "The Shawshank Redemption",
        "plot": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "genres": ["Drama"],
        "casts": ["Tim Robbins", "Morgan Freeman"],
    },
    {
        "name": "Forrest Gump",
        "plot": "Forrest Gump, while not intelligent, has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.",
        "genres": ["Drama", "Romance"],
        "casts": ["Tom Hanks", "Robin Wright"],
    },
]


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
    movie = payload.dict()
    movies_length = len(fake_movie_db)
    if 0 <= id <= movies_length:
        fake_movie_db[id] = movie
        return None
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Movie with given id not found"
    )


@movies.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movie with given id not found",
        )

    return await db_manager.delete_movie(id)
