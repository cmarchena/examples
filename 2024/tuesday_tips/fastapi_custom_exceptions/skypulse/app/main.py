from fastapi import FastAPI

from app.api.routes.router import base_router as router

from core.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION


app = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
app.include_router(router, prefix=API_PREFIX)



