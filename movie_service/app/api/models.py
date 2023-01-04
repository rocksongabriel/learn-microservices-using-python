from pydantic import BaseModel


class MovieBase(BaseModel):
    name: str
    plot: str
    genres: list[str]
    casts_id: list[int]


class MovieIn(MovieBase):
    pass


class MovieOut(MovieBase):
    id: int


class MovieUpdate(BaseModel):
    name: str | None = None
    plot: str | None = None
    genres: list[str] | None = None
    casts_id: list[int] | None = None
