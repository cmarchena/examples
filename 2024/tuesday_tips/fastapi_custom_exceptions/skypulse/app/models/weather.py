from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from . import Base


class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, ForeignKey('cities.id'))
    temperature = Column(Integer)
    humidity = Column(Integer)
    description = Column(String)

    city = relationship("City", back_populates="weathers")
