from sqlalchemy import Column, Integer, String, DateTime, Boolean
from database.base import Base
from sqlalchemy.dialects.postgresql import ARRAY


class Building(Base):
    __tablename__ = 'buildings'
    id = Column(Integer, primary_key=True, index=True)
    residential_complex = (Column(String(255), nullable=False))
    building = Column(String(10), nullable=False)
    entrance = Column(Integer, nullable=False)
    floor = Column(Integer, nullable=False)
    flat_num = Column(Integer, nullable=False)
    area = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String(400), nullable=False)
    photo_links = Column(ARRAY(String), nullable=False)
    rooms = Column(Integer, nullable=False)
    address = Column(String(255), nullable=False,
                     server_default='улица Неизвестная 1')
