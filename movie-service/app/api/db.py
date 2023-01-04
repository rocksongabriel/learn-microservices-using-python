import os

from databases import Database
from dotenv import load_dotenv
from sqlalchemy import ARRAY, Column, Integer, MetaData, String, Table, create_engine

load_dotenv()

DATABASE_URI = os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI)
metadata = MetaData()


movies = Table(
    "movies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("plot", String(250)),
    Column("genres", ARRAY(String)),
    Column("casts", ARRAY(String)),
)

database = Database(DATABASE_URI)
