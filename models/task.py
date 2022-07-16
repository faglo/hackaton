from sqlalchemy import Column, Integer, String, DateTime, Boolean
from database.base import Base
from sqlalchemy.dialects.postgresql import ARRAY


class Task(Base):
    __tablename__ = 'buildings'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    agent_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
