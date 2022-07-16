from fastapi import APIRouter, Depends
from schemas.building import Building
from repository.building import BuildingRepository
from services.building import get_building_service
from typing import List

router = APIRouter()


@router.get("/", response_model=List[Building])
def get_by_filter(
    residential_complex: str = None,
    building: str = None,
    area_from: int = None,
    area_to: int = None,
    rooms: int = None,
    floor_from: int = None,
    floor_to: int = None,
    price_from: int = None,
    price_to: int = None,
    buildings: BuildingRepository = Depends(get_building_service)
):
    return buildings.get_by_filters(
        residential_complex=residential_complex,
        building=building,
        area_from=area_from,
        area_to=area_to,
        rooms=rooms,
        floor_from=floor_from,
        floor_to=floor_to,
        price_from=price_from,
        price_to=price_to,
    )


@router.get("/filters")
def get_filter_props(buildings: BuildingRepository = Depends(get_building_service)):
    residential_complexes = buildings.get_residential_complexes()
    buildings = buildings.get_buildings()

    return {
        "residential_complexes": residential_complexes,
        "buildings": buildings,
    }
