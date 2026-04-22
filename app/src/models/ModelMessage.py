import time
from email.policy import default
from typing import Optional, List

from sqlalchemy import BigInteger, JSON
from sqlmodel import Field, SQLModel

from app.src.db import engine


# --- 2. 消息 ---
class MessageComment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # [新增] 主键
    
    # [优化] 关联用户：存 OpenID 而不是整个对象
    # 这样可以通过 user_openid 去 User 表查最新的昵称和头像
    user_openid: str = Field(index=True)
    
    content: str  # 消息内容
    is_read: bool = Field(default=False)  # [优化] 命名规范化
    
    # [优化] 时间戳：使用 datetime 类型，数据库会自动处理时区
    created_at: int = Field(
        default_factory=lambda: int(time.time() * 1000),
        sa_type=BigInteger,
        index=True  # 加上索引，查询“最近的消息”会非常快
    )
    
    # [优化] 图片列表：存为 JSON 字符串
    # SQLModel/SQLAlchemy 支持直接存 list，底层会自动转成 JSON
    image_urls: List[str] = Field(
        default=[],
        sa_type=JSON
    )
    
    # [新增] 软删除标记 (可选)
    is_deleted: bool = Field(default=False)
    
    
def create_db_and_tables():
    print("创建表 MessageComment")
    SQLModel.metadata.create_all(engine)
