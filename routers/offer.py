from fastapi import APIRouter, Depends
from schemas.offer import Offer
from repository.offer import OfferRepository
from services.offer import get_offer_service

router = APIRouter()


@router.post("/")
def create_offer(
    object: Offer,
    offers: OfferRepository = Depends(get_offer_service)
):
    return offers.create(object.building_ids)


@router.get("/{offer_id}")
def get_by_id(offer_id: int, offers: OfferRepository = Depends(get_offer_service)):
    return offers.get_buildings_by_offer_id(offer_id)
