from fastapi import FastAPI  # ,Request
from app.routes import user, ai
from contextlib import asynccontextmanager
import time
from fastapi.middleware.cors import CORSMiddleware
from app.error.exceptions import (
    AiModelIsNotAvaible,
    DbError,
    ServiceFailed,
    UserNotFound,
    WrongPassword,
)
from app.error.exception_handler import (
    ai_model_is_not_avaible_handler,
    db_error_handler,
    service_failed_handler,
    user_not_found_handler,
    wrong_password_handler,
)
from .Repositories import router as repo_router

# import os
# import asyncio
# from .Dependencies.secrets import setting
# from app.config.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("\nhello monkeys\n ")
    # app.state.learning = "the honored one"
    # k= settings()
    # print(k)
    # print(settings.groq_api_key)
    yield
    # await asyncio.sleep(1)
    print("good bye monkeys")


app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def my_middleware(request, call_next):
    start = time.perf_counter()
    print("BEFORE")
    # await asyncio.sleep(3)
    response = await call_next(request)

    duration = time.perf_counter() - start
    print(f"\nAFTER\n\n request took { duration*1000:.2f} milliseconds\n")
    return response


app.add_exception_handler(UserNotFound, user_not_found_handler)
app.add_exception_handler(WrongPassword, wrong_password_handler)
app.add_exception_handler(DbError, db_error_handler)
app.add_exception_handler(AiModelIsNotAvaible, ai_model_is_not_avaible_handler)
app.add_exception_handler(ServiceFailed, service_failed_handler)

app.include_router(user.router)
app.include_router(ai.router)
app.include_router(repo_router)


@app.post("/work")
def sign_up_e():
    return {"name": "wiw"}


# def signup_ep(  username: Annotated [str , Path (max_length=  50)  ] ,
# birthday:Annotated[date ,Query( description="YYYY-MM-DD])):
