from typing import Optional, List
from pydantic import BaseModel


class Offer(BaseModel):
    id: Optional[int]
    building_ids: List[int]
