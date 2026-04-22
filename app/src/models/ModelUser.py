from typing import Optional, Annotated

from fastapi.params import Depends
from sqlmodel import Field, Session, SQLModel

from app.src.db import engine
from app.src.models.model_Hero import get_session


class School(SQLModel, table=True):
    """学校表：用于隔离数据"""
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)          # 学校名，如 "清华大学"
    code: str = Field(max_length=20)          # 简码，如 "thu"


class User(SQLModel, table=True):
    # --- 基础身份 ---
    id: Optional[int] = Field(default=None, primary_key=True)
    openid: str = Field(unique=True, index=True)
    
    # 关联学校 (外键)
    school_id: Optional[int] = Field(default=None, foreign_key="school.id")
    
    # --- 校园核心信息 ---
    # 学号用于验证身份，unique=True 防止同一个学生注册多次
    student_id: Optional[str] = Field(default=None, unique=True, index=True, max_length=20)
    
    # 宿舍楼是校园跑腿的核心筛选维度
    dorm_building: Optional[str] = Field(default=None, max_length=50)
    
    # --- 展示信息 ---
    # 修正：去掉了重复定义的 nick_name 和 avatar_url
    nick_name: str = Field(default="同学")
    avatar_url: Optional[str] = Field(default=None)
    
    # --- 联系方式与隐私 ---
    # 修正：去掉了错误的 default=Field，改为 default=False
    # 含义：默认不公开联系方式，保护隐私
    is_public_contact: bool = Field(default=False)
    
    contact_info: Optional[str] = Field(default=None, max_length=20)
    
    # --- 信用与统计 ---
    score: int = Field(default=100)
    count_service: int = Field(default=0)
    avg_rating: float = Field(default=5.0)
    
    # --- 钱包 ---
    # 建议加上注释，单位是分
    balance: int = Field(default=0)
    
    # --- 状态 ---
    is_banned: bool = Field(default=False)
    created_at: int
    
def create_db_and_tables():
    print("创建表 User")
    SQLModel.metadata.create_all(engine)
if __name__ == "__main__":
    create_db_and_tables()
SessionDep = Annotated[Session, Depends(get_session)]