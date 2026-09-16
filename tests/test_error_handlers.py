import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.error.exceptions import (
    UserNotFound,
    WrongPassword,
    DbError,
    AiModelIsNotAvaible,
)
from app.error.exception_handler import (
    user_not_found_handler,
    wrong_password_handler,
    db_error_handler,
    ai_model_is_not_avaible_handler,
)


def test_exception_classes_exist():
    assert UserNotFound.__name__ == "UserNotFound"
    assert WrongPassword.__name__ == "WrongPassword"
    assert DbError.__name__ == "DbError"
    assert AiModelIsNotAvaible.__name__ == "AiModelIsNotAvaible"


def test_handlers_return_expected_status_and_detail():
    app = FastAPI()
    app.add_exception_handler(UserNotFound, user_not_found_handler)
    app.add_exception_handler(WrongPassword, wrong_password_handler)
    app.add_exception_handler(DbError, db_error_handler)
    app.add_exception_handler(AiModelIsNotAvaible, ai_model_is_not_avaible_handler)

    @app.get("/user-not-found")
    def user_not_found():
        raise UserNotFound()

    @app.get("/wrong-password")
    def wrong_password():
        raise WrongPassword()

    @app.get("/db-error")
    def db_error():
        raise DbError()

    @app.get("/ai-model")
    def ai_model():
        raise AiModelIsNotAvaible()

    client = TestClient(app)

    assert client.get("/user-not-found").status_code == 404
    assert client.get("/wrong-password").status_code == 401
    assert client.get("/db-error").status_code == 500
    assert client.get("/ai-model").status_code == 503
