from typing import Optional, List
from pydantic import BaseModel


class Building(BaseModel):
    id: Optional[int]
    residential_complex: str
    building: str
    entrance: int
    floor: int
    flat_num: int
    area: int
    price: int
    photo_links: List[str]
    rooms: int
