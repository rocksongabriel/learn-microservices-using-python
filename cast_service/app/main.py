from fastapi import FastAPI
from .api.db import database, engine, metadata, casts
from .api.casts import casts

metadata.create_all(engine)

app = FastAPI()
app.include_router(casts, prefix="/api/v1/casts", tags=["Casts"])


@app.on_event("startup")
async def startup():
    return await database.connect()


@app.on_event("shutdown")
async def shutdown():
    return await database.disconnect()
