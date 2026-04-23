from typing import Annotated, Any, Sequence

from fastapi import HTTPException, Query
from fastapi import UploadFile, File, APIRouter
from fastapi.sse import EventSourceResponse
from sqlmodel import select
from starlette.responses import StreamingResponse

from app.src.services.server_auth import server_auth


router = APIRouter()


@router.post("/login", tags=["这是接口标签"], summary="这是接口注释")
async def user_login(
        file: UploadFile | None = File(default=None)
):
    data = await server_auth(file)

    return {"message": data}

from pydantic import BaseModel
import json
import asyncio


class Item(BaseModel):
    name: str
    description: str | None


items = [
    Item(name="Plumbus", description="A multi-purpose household device."),
    Item(name="Portal Gun", description="A portal opening device."),
    Item(name="Meeseeks Box", description="A box that summons a Meeseeks."),
]

from collections.abc import AsyncIterable


@router.get("/liu2", response_class=EventSourceResponse)
async def sse_items() -> AsyncIterable[Item]:
    for item in items:
        yield item
        await asyncio.sleep(1)


@router.get("/liu")
async def read_liu():
    async def event_generator():
        for item in items:
            yield json.dumps(item.model_dump()) + "\n"
            await asyncio.sleep(1)  # 模拟流式

    return StreamingResponse(event_generator(), media_type="application/json")
