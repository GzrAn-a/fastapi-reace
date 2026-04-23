from pydantic import BaseModel


class SchemaOrderIndex(BaseModel):
    """小程序首页 抢单返回schemas"""
    order_id: int # 订单号
    user_id: int  # 发布者id
    avatar:str # 发布者 头像
    user_name: str  # 发布者名字
    from_address: str # 取货地
    to_address: str  # 送货地址
    start_time:int  # 开始时间戳
    end_time:int  # 结束时间戳
    money:int  # 本单价格
    status:int # 0 待接单 1 配送中 2 已送达 3 已完成 4 待评价
    distance:int # 距离米
