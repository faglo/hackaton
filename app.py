from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from routers.building import router as building_router
from routers.offer import router as offer_router

app = FastAPI()


@app.on_event("startup")
def startup_event():
    logger.add(
        "./assets/logs/latest.log", rotation="200 KB", enqueue=True, level="INFO"
    )
    logger.info("App started")


app.include_router(building_router, prefix="/building")
app.include_router(offer_router, prefix="/offer")
app.add_middleware(CORSMiddleware, allow_origins=[
                   "*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],)
