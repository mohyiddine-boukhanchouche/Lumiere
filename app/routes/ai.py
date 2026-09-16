from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from ..Dependencies.secrets import m_setting
from ..error.exceptions import ServiceFailed
from ..config import Settings
from typing import Annotated
from ..service.ai_ser import ai_service
from ..schemas.user import Cchat, error_life

# import time
# from starlette.concurrency import run_in_threadpool

router = APIRouter(prefix="/ai")


@router.post(
    "/chat",
    response_model=str,
    status_code=201,
    responses={404: {"model": error_life, "description": "la vie happend"}},
)
async def chatting(
    q: Cchat,
    k: Annotated[Settings, Depends(m_setting)],
    background_tasks: BackgroundTasks,
):
    # await run_in_threadpool(time.sleep, 3)
    background_tasks.add_task(ai_service.f)

    try:
        a = await ai_service.ask(q, k)
    except Exception as e:
        raise ServiceFailed()
    # if "input" in a:
    #    raise HTTPException(404, a["input"]["error"]["message"])
    return a["choices"][0]["message"]["content"]
    # return a


# except ValueError:
# return {"response": response.text}
