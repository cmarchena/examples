from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db_session
from app.models import Weather
from app.schemas import WeatherCreate, WeatherSchema
from sqlalchemy.future import select


router = APIRouter()


@router.post("/weather/", response_model=WeatherSchema)
async def create_weather(
    weather: WeatherCreate, db: AsyncSession = Depends(get_db_session)
):
    db_weather = Weather.model_dump(weather)
    db.add(db_weather)
    await db.commit()
    await db.refresh(db_weather)
    return db_weather


@router.get("/weather/", response_model=list[WeatherSchema])
async def get_weather(db: AsyncSession = Depends(get_db_session)):
    async with db as session:
        result = await session.execute(select(Weather))
        weather_records = result.scalars().all()
        return weather_records
