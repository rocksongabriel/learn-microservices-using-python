from databases import Database
from sqlalchemy import ARRAY, Column, Integer, MetaData, String, Table, create_engine


DATABASE_URL = "postgresql://test_user1:testpass1234@localhost:5433/movies_db"

engine = create_engine(DATABASE_URL)
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

database = Database(DATABASE_URL)
