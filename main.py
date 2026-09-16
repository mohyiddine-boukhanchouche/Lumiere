from fastapi import FastAPI

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

app = FastAPI()

app.add_exception_handler(UserNotFound, user_not_found_handler)
app.add_exception_handler(WrongPassword, wrong_password_handler)
app.add_exception_handler(DbError, db_error_handler)
app.add_exception_handler(AiModelIsNotAvaible, ai_model_is_not_avaible_handler)
app.add_exception_handler(ServiceFailed, service_failed_handler)


def main():
    print("Hello from phase1-b!")


if __name__ == "__main__":
    main()
