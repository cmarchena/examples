from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    country = Column(String)
    population = Column(Integer, nullable=True)

    # Relationship with weather
    weathers = relationship("Weather", back_populates="city")
