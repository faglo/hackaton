from typing import Optional, List
from pydantic import BaseModel


class Building(BaseModel):
    id: Optional[int]
    building_ids: List[int]
