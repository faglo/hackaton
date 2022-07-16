from sqlalchemy import Column, Integer, String, DateTime, Boolean
from database.base import Base
from sqlalchemy.dialects.postgresql import ARRAY


class Building(Base):
    __tablename__ = 'buildings'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    building_type = Column(String(255), nullable=False)
    realisation_type = Column(String(255), nullable=False)
    cost = Column(Integer, nullable=False)
    photo_links = Column(ARRAY(String(255)), nullable=False)
    city = Column(String(255), nullable=False)
    flat_complex = Column(String(255), nullable=False)
    site_description = Column(String(255), nullable=False)
    internal_description = Column(String(255), nullable=False)
    floor_area = Column(Integer, nullable=False)
    room_count = Column(Integer, nullable=False)
    floor = Column(Integer, nullable=False)
    total_floor_count = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
