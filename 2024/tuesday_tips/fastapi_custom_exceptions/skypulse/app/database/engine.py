from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "sqlite+aiosqlite:///./app/database/skypulse.db"  # Updated for async SQLite
engine = create_async_engine(DATABASE_URL, echo=True)
