from typing import Optional, List
from pydantic import BaseModel


class Building(BaseModel):
    id: Optional[int]
    name: str
    category: str
    building_type: str
    realisation_type: str
    cost: int
    photo_links: List[str]
    city: str
    flat_complex: str
    site_description: str
    internal_description: str
    floor_area: int
    room_count: int
    floor: int
    total_floor_count: int