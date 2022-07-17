from sqlalchemy import Column, Integer
from database.base import Base
from sqlalchemy.dialects.postgresql import ARRAY


class Offer(Base):
    __tablename__ = 'offers'
    id = Column(Integer, primary_key=True, index=True)
    building_ids = Column(ARRAY(Integer), nullable=False)
