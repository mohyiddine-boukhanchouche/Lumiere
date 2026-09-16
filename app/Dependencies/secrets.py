from fastapi import Depends
from ..config import settings, Settings

# from dotenv import load_dotenv
# import os

# from pathlib import Path

# env_path = Path(__file__).resolve().parent.parent.parent / ".env"
# load_dotenv()
# dotenv_path=env_path


def m_setting() -> Settings:
    return settings
