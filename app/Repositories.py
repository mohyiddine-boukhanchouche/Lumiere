from typing import Any

from fastapi import APIRouter
from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import sessionmaker
from .models import User, Question
from .schemas.user import Userlogin

engine = create_engine("postgresql+psycopg:///mark1?host=/var/run/postgresql")

router = APIRouter()

SessionLocal = sessionmaker(bind=engine)


class mydb:
    @staticmethod
    def login(user_login: Userlogin):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM users WHERE username = :i"),
                {"i": "mahi"},
            )
            row = result.mappings().fetchone()
        return dict(row) if row is not None else None

    @staticmethod
    def pretest_query():
        """Simple learning query for testing SQLAlchemy and database output."""
        with engine.connect() as connection:
            result = connection.execute(
                text(
                    "SELECT id, username, note FROM users WHERE password = :pw ORDER BY id LIMIT 10"
                ),
                {"pw": "hashed_pw_3"},
            )
            rows = result.mappings().all()
        return [dict(row) for row in rows]

    @staticmethod
    def get_user(y: Userlogin):
        with SessionLocal() as session:
            stmt = select(User).where(
                User.username == y.username  # , User.password == y.password
            )
            return session.scalars(stmt).first()

    @staticmethod
    def grace():
        with SessionLocal() as session:
            stmt = select(User, Question).join(User.Question)
