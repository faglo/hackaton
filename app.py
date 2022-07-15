from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

app = FastAPI()


@app.on_event("startup")
def startup_event():
    logger.add(
        "./assets/logs/latest.log", rotation="200 KB", enqueue=True, level="INFO"
    )
    logger.info("App started")


app.add_middleware(CORSMiddleware, allow_origins=[
                   "*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],)


@app.middleware("http")
async def check_token(r: Request, call_next):
    resp: Response = await call_next(r)
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Methods"] = "*"
    resp.headers["Access-Control-Allow-Headers"] = "*"

    if (
        "/login" in str(r.url)
    ):
        return resp

    error = JSONResponse(
        status_code=401,
        content={"success": False, "error": "No Authentication header"},
        headers={"Access-Control-Allow-Origin": "*"},
    )

    try:
        if not verify_jwt(r.headers["authentication"]):
            logger.error("JWT Error!")
            return error
    except KeyError:
        logger.error("Headers Error!")
        return error
    return resp


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(account.router)
app.include_router(action_log.router)
app.include_router(user.router)
app.include_router(config.router)
app.include_router(mail_log.router)
app.include_router(template.router)
app.include_router(projects.router)
app.include_router(mailing.router)


class SPAStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope):
        response = await super().get_response(path, scope)
        if response.status_code == 404:
            response = await super().get_response(".", scope)
        return response


if not DEBUG:
    app.mount(
        "/", SPAStaticFiles(directory="./frontend/dist", html=True), name="mainapp"
    )

if __name__ == "__main__":
    uvicorn.run(app, port=PORT)
