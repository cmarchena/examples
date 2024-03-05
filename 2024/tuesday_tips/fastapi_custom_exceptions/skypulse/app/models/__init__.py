from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    country = Column(String)
    population = Column(Integer, nullable=True)

    # Relationship with weather
    weathers = relationship("Weather", back_populates="city")

class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, ForeignKey('cities.id'))
    temperature = Column(Integer)
    humidity = Column(Integer)
    description = Column(String)

    city = relationship("City", back_populates="weathers")
