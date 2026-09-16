from fastapi import APIRouter, Request  # , Depends
from ..schemas.user import UserCreate, Userlogin
from ..error.exceptions import *
from ..Repositories import mydb

router = APIRouter(prefix="/users")


@router.post("/signup")
def signup(user: UserCreate, request: Request):
    if user.username == "zaki":
        raise UserNotFound()
    return {
        "name": user.username,
        "Anniversaire": user.birthday,
        # "aplication state": request.app.state.learning,
    }


@router.post("/signin")
def signin(u: Userlogin):
    user = mydb.get_user(u)
    return {"name": user.username, "id": user.id}


@router.get("/pretest")
def pretest_route():
    return {
        "data": mydb.pretest_query(),
    }


@router.post("/login-db")
def login(y: Userlogin):
    return {"id": mydb.get_user.id}
