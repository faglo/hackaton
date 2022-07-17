from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from fastapi.staticfiles import StaticFiles
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


class SPAStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope):
        response = await super().get_response(path, scope)
        if response.status_code == 404:
            response = await super().get_response(".", scope)
        return response


app.mount(
    "/", SPAStaticFiles(directory="./frontend/dist", html=True), name="mainapp"
)
