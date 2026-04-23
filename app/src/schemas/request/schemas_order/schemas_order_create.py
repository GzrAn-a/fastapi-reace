from typing import List

from pydantic import BaseModel

class RequestOrderCreate(BaseModel):
    """接受前端发来的创建 订单"""
    from_address: str # 取货地址
    to_address: str  # 收货地址
    sth_image:List[str] # 货物图片
    money:int
    tips:List[str] # 备注标签
    end_time:int  # 截至时间戳
    tips_text:str  # 备注文字