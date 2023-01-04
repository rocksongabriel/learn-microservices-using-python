from dotenv import load_dotenv
import os
from sqlalchemy import Column, Table, Integer, String, MetaData, create_engine
from databases import Database

load_dotenv()

DATABASE_URI = os.getenv("CASTS_DATABASE_URI")
database = Database(DATABASE_URI)
engine = create_engine(DATABASE_URI)
metadata = MetaData()


casts = Table(
    "casts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("nationality", String(50)),
)
