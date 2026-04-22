# 订单模型
import random
from typing import Optional, List

from sqlalchemy import BigInteger ,JSON ,Column,String# 👈 2. 导入 JSON 类型
from sqlmodel import SQLModel, Field

from app.src.db import engine


class ModelProject(SQLModel,table=True):
    
    id: Optional[int] = Field(default=None, primary_key=True)  # 主键
    project_id: str = Field(unique=True, index=True)  # 业务订单号 (如: "ORD_20231027_001")
    
    # 核心隔离字段：订单属于哪个学校
    school_id: Optional[int] = Field(default=None, foreign_key="school.id")
    
    # 关联人员
    publisher_openid: str = Field(index=True)  # 发布者 (出钱的人)
    receiver_openid: Optional[str] = Field(default=None, index=True)  # 接单者 (跑腿的人，接单前为空)
    
    # --- 3. 订单状态 ---
    # 0: 待接单, 1: 待取货, 2: 配送中, 3: 已完成, 4: 已取消, 5: 申诉中
    status: int = Field(default=0, index=True,description="订单状态: 0-待接单, 1-待取货, 2-配送中, 3-已完成, 4-已取消")
    
    from_address: str =Field(sa_column=Column(String(255),comment="取货详细地址")) # 取货地址
    to_address: str = Field(
        title="送货地址",
        description="收货人的详细门牌号地址",
        max_length=200
    ) # 送货地址
    from_phone: str  # 取货联系人电话 (重要！)
    to_phone: str  # 收货联系人电话 (重要！)
    
    item_type: str  # 物品类型 (文件/蛋糕/钥匙/其他)
    item_weight: str  # 重量/规格 (如 "5kg以内")
    tags: Optional[List[str]] = Field(
        default=[],
        sa_type=JSON  # 👈 关键：明确告知 SQLAlchemy 这是一个 JSON 字段
    )
    
    price: int  # 基础配送费 (分)
    tip_amount: int = Field(default=0)  # 额外打赏 (分)
    
    # --- 7. 时间 ---
    created_at: int = Field(..., sa_type=BigInteger)  # 下单时间
    deadline: int = Field(..., sa_type=BigInteger)  # 截止时间
    
    # --- 8. 凭证 (可选) ---
    # 如果是贵重物品，发布者可能会传一张物品照片
    item_image: Optional[str] = Field(default=None)
    
    # 默认生成一个随机6位数字，下单时生成
    verify_code: str = Field(default_factory=lambda: str(random.randint(100000, 999999)), max_length=6)
    
    # --- 新增：核销时间 (可选) ---
    # 如果这个字段不为空，说明订单已经通过验证码完成了
    verified_at: Optional[int] = Field(default=None, sa_type=BigInteger)

def create_db_and_tables():
    print("创建表 ModelProject")
    SQLModel.metadata.create_all(engine)
