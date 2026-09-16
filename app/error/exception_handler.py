from fastapi import Request
from fastapi.responses import JSONResponse

from .exceptions import (
    AiModelIsNotAvaible,
    DbError,
    ServiceFailed,
    UserNotFound,
    WrongPassword,
)


async def user_not_found_handler(request: Request, exc: UserNotFound):
    return JSONResponse(status_code=404, content={"detail": "user not found"})


async def wrong_password_handler(request: Request, exc: WrongPassword):
    return JSONResponse(status_code=401, content={"detail": "wrong password"})


async def db_error_handler(request: Request, exc: DbError):
    return JSONResponse(status_code=500, content={"detail": "db error"})


async def ai_model_is_not_avaible_handler(request: Request, exc: AiModelIsNotAvaible):
    return JSONResponse(status_code=503, content={"detail": "ai model is not avaible"})


async def service_failed_handler(request: Request, exc: ServiceFailed):
    return JSONResponse(status_code=503, content={"detail": "service failed"})
