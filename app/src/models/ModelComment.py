from email.policy import default
from typing import Optional, List

from sqlalchemy import BigInteger,JSON
from sqlmodel import SQLModel, Field

from app.src.db import engine


#

class ModelComment(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    
    # 评论人
    user_openid:str = Field(index=True)
    is_public:bool = True  # 默认不匿名
    # 被论人
    target_user_openid:str = Field(index=True)
    
    target_id:str = Field(index=True) # 订单ID
    
    content:str # 评论内容
    
    star:int # 星 数量
    
    created_at:int = Field(...,sa_type=BigInteger)
    
    images: List[str] = Field(
        default=[],
        sa_type=JSON
    )  # 晒图列表
    
    
def create_db_and_tables():
    print("创建表ModelComment")
    SQLModel.metadata.create_all(engine)
