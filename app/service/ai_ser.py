from fastapi import BackgroundTasks, FastAPI
from ..schemas.user import Cchat
from fastapi import Depends
from typing import Annotated
import httpx
from ..Dependencies.secrets import m_setting
from ..config import Settings
import time


class ai_service:

    @staticmethod
    async def ask(q: Cchat | str, k: Annotated[Settings, Depends(m_setting)]):
        GROQ_API_KEY = k.groq_api_key
        if isinstance(q, Cchat):
            q = q.Question
        async with httpx.AsyncClient() as client:
            response = await client.request(
                method="POST",
                url="https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {GROQ_API_KEY }",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "openai/gpt-oss-20b",
                    "messages": [{"role": "user", "content": q}],
                },
            )
            return response.json()

    @staticmethod
    def f():
        time.sleep(5)
        print("\n   AS U COMMAND MY LORD\n")

    @staticmethod
    async def ask_gentaly(
        q: Cchat | str,
        k: Annotated[Settings, Depends(m_setting)],
        background_tasks: BackgroundTasks,
    ):
        a = await ai_service.ask(q, k)
        background_tasks.add_task(ai_service.f())
        return a.json()
