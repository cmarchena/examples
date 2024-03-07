from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db_session
from app.models import City
from app.schemas import CityCreate, CitySchema


router = APIRouter()

@router.post("/cities/", response_model=CitySchema)
async def create_city(city: CityCreate, db: AsyncSession = Depends(get_db_session)):
    db_city = City.model_dump(city)
    db.add(db_city)
    await db.commit()
    await db.refresh(db_city)
    return db_city

@router.get("/cities/", response_model=list[CitySchema])
async def get_cities(db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(City))
    cities = result.scalars().all()
    return cities
