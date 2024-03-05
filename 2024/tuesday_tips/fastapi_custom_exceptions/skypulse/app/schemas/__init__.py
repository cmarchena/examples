from pydantic import BaseModel
from typing import Optional

class CityBase(BaseModel):
    name: str
    country: str
    population: Optional[int] = None

class CityCreate(CityBase):
    pass

class CitySchema(CityBase):
    id: int

    class Config:
        orm_mode = True

class WeatherBase(BaseModel):
    city_id: int
    temperature: int
    humidity: int
    description: str

class WeatherCreate(WeatherBase):
    pass

class WeatherSchema(WeatherBase):
    id: int

    class Config:
        orm_mode = True
