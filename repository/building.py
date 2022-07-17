from repository.base import BaseRepository
from models.building import Building


class BuildingRepository(BaseRepository):
    def get_all(self):
        return self.session.query(Building).all()

    def get_by_id(self, id):
        return self.session.query(Building).filter(Building.id == id).first()

    def create(self, data):
        building = Building(**data)
        self.session.add(building)
        self.session.commit()
        return building

    def update(self, id, data):
        building = self.session.query(
            Building).filter(Building.id == id).first()
        if building:
            building.__dict__.update(data)
            self.session.commit()
            return building
        return None

    def delete(self, id):
        building = self.session.query(
            Building).filter(Building.id == id).first()
        if building:
            self.session.delete(building)
            self.session.commit()
            return building
        return None

    def get_by_filters(
        self,
        residential_complex: str = "",
        building: str = "",
        area_from: int = 0,
        area_to: int = 0,
        rooms: int = 0,
        floor_from: int = 0,
        floor_to: int = 0,
        price_from: int = 0,
        price_to: int = 0,
    ):
        query = self.session.query(Building)
        if residential_complex != "":
            query = query.filter(
                Building.residential_complex == residential_complex)
        if building != "":
            query = query.filter(Building.building == building)
        if area_from != 0:
            query = query.filter(Building.area >= area_from)
        if area_to != 0:
            query = query.filter(Building.area <= area_to)
        if rooms != 0:
            query = query.filter(Building.rooms == rooms)
        if floor_from != 0:
            query = query.filter(Building.floor >= floor_from)
        if floor_to != 0:
            query = query.filter(Building.floor <= floor_to)
        if price_from != 0:
            query = query.filter(Building.price >= price_from)
        if price_to != 0:
            query = query.filter(Building.price <= price_to)
        return query.all()

    def get_residential_complexes(self):
        return self.session.query(
            Building.residential_complex).distinct().all()

    def get_buildings(self):
        return self.session.query(
            Building.building).distinct().all()
