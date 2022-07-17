from repository.base import BaseRepository
from models.offer import Offer
from models.building import Building


class OfferRepository(BaseRepository):
    def get_all(self):
        return self.session.query(Offer).all()

    def get_by_id(self, id):
        return self.session.query(Offer).filter(Offer.id == id).first()

    def create(self, data):
        Offer = Offer(**data)
        self.session.add(Offer)
        self.session.commit()
        return Offer

    def update(self, id, data):
        Offer = self.session.query(
            Offer).filter(Offer.id == id).first()
        if Offer:
            Offer.__dict__.update(data)
            self.session.commit()
            return Offer
        return None

    def delete(self, id):
        Offer = self.session.query(
            Offer).filter(Offer.id == id).first()
        if Offer:
            self.session.delete(Offer)
            self.session.commit()
            return Offer
        return None

    def get_buildings_by_offer_id(self, offer_id: int):
        building_ids = self.session.query(
            Offer.building_ids).filter(Offer.id == offer_id).first()
        if building_ids:
            print(building_ids)
            return self.session.query(Building).filter(
                Building.id.in_(building_ids)).all()
        else:
            return []
