from repository.building import BuildingRepository
from database.connections import get_database_connection


def get_building_service() -> BuildingRepository:
    db = get_database_connection()
    return BuildingRepository(next(db))
