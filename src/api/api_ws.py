from fastapi import APIRouter
from starlette.websockets import WebSocket

router = APIRouter()


@router.websocket('/ws')
async def my_socker(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
