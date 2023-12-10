from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.config import CONFIG


class Base(DeclarativeBase):
    pass


engine = create_async_engine(CONFIG.PG_DSN)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession)
