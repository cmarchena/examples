from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.exceptions import EntityDoesNotExistError, ServiceError


async def service_error_handler(request: Request, _exc: ServiceError):
    return JSONResponse(
        status_code=500,
        content={
            "detail": "We're currently experiencing connection issues. Please try again in a few moments"
        },
    )


async def entity_does_not_exist_error_handler(request: Request, _exc: EntityDoesNotExistError):
    return JSONResponse(
        status_code=404, content={"detail": "The requested entity does not exist."}
    )
