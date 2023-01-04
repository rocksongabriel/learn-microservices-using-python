from fastapi import APIRouter, status, HTTPException
from .models import CastIn, CastOut
from . import db_manager


casts = APIRouter()


@casts.post("/", status_code=status.HTTP_201_CREATED)
async def add_cast(payload: CastIn):
    cast_id = await db_manager.add_cast(payload)

    response = {"id": cast_id, **payload.dict()}

    return response


@casts.get("/{id}", response_model=CastOut)
async def get_cast(id: int):
    cast = db_manager.get_cast(id)
    if not cast:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Cast with id {id} not found"
        )
    return await db_manager.get_cast(id)


@casts.get("/", response_model=list[CastOut])
async def get_casts():
    return await db_manager.all_casts()
