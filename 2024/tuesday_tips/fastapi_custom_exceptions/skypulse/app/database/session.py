from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, AsyncGenerator
from sqlalchemy.orm import sessionmaker
from .engine import engine

async_session_factory = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)  # type: ignore


# Dependency to get DB session
async def get_db_session() -> AsyncGenerator[Any, AsyncSession]:
    async with async_session_factory() as session:  # type: ignore
        yield session
