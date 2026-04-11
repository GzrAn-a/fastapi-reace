

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


class SocketData(BaseModel):
    """用户输入"""
    name: str
    price: float
    is_offer: bool
class WebSocketData(BaseModel):
    now:str
    data: SocketData