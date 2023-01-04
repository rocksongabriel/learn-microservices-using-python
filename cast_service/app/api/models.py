from pydantic import BaseModel


class CastBase(BaseModel):
    name: str
    nationality: str


class CastIn(CastBase):
    pass


class CastOut(CastBase):
    id: int


class CastUpdate(CastBase):
    name: str | None = None
