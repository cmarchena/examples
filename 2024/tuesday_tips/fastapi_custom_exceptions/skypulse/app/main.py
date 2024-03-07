from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.routes.router import base_router as router
from app.exception_handlers.exception_handlers import (
    entity_does_not_exist_error_handler,
    service_error_handler,
)
from app.exceptions.exceptions import EntityDoesNotExistError, ServiceError
from core.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from app.database.session import sessionmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Function that handles startup and shutdown events.
    To understand more, read https://fastapi.tiangolo.com/advanced/events/
    """
    yield
    if sessionmanager._engine is not None: # noqa
        await sessionmanager.close()

app = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
app.include_router(router, prefix=API_PREFIX)

app.add_exception_handler(
    exc_class_or_status_code=EntityDoesNotExistError,
    handler=entity_does_not_exist_error_handler,
)

app.add_exception_handler(
    exc_class_or_status_code=ServiceError,
    handler=service_error_handler,
)
