from repository.offer import OfferRepository
from database.connections import get_database_connection


def get_offer_service() -> OfferRepository:
    db = get_database_connection()
    return OfferRepository(next(db))
