from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from .environment import settings

user = settings.get("database").get("user")
password = settings.get("database").get("password")
host = settings.get("database").get("host")
database_name = settings.get("database").get("name")

DATABASE_URL = f"postgresql+asyncpg://{user}:{password}@{host}/{database_name}"
engine = create_async_engine(DATABASE_URL, future=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()
