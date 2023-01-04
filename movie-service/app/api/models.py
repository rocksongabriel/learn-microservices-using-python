from pydantic import BaseModel

class MovieBase(BaseModel):
    name: str
    plot: str
    genres: list[str]
    casts: list[str]

class MovieIn(MovieBase):
    pass

class MovieOut(MovieBase):
    id: int

    
class MovieUpdate(BaseModel):
    name: str | None = None
    plot: str | None = None
    genres: list[str] | None = None
    casts: list[str] | None = None