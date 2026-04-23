import hashlib
import random
import time
import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.src.schemas.request.schemas_order.schemas_order_create import RequestOrderCreate
from app.src.models.ModelProject import ModelProject
from app.src.models.ModelUser import ModelUser
from app.src.db  import get_session

router = APIRouter()


@router.post("/order", summary="创建订单")
async def create_order(
        order_data: RequestOrderCreate,
        session: Session = Depends(get_session) # 不能这样带有括号 Depends(get_session())
):
    # 1 获取用户id 123
    request_user_id = "4"
    user_statement = select(ModelUser).where(ModelUser.id == request_user_id)  # 查询出 对应的用户
    user_info: ModelUser = session.exec(user_statement).first()  # 转化为 用户模型 实力
    if user_info is None:
        return {"message": '用户未注册'}
    if user_info.school_id ==0:
        return {"message": "您的学校信息未通过管理员审核"}
    # 2 订单号
    project_id = str(uuid.uuid4())  # 长度 36 位，全球唯一
    # 3. 数据映射：将 Schema 转换为 Model
    new_order = ModelProject(
        project_id=project_id,
        publisher_openid=user_info.openid,
        status=0,
        school_id =user_info.school_id,
        from_address=order_data.from_address,
        to_address=order_data.to_address,
        # 注意：你需要补全 Schema 中缺少的 from_phone 和 to_phone，或设置默认值
        from_phone="00000000000",
        to_phone="00000000000",
        item_type="其他",  # 根据你的 Schema 可能需要补全
        item_weight="5kg以内",
        tags=order_data.tips,  # 映射标签
        price=order_data.money,
        tip_amount=0,  # 如果 Schema 中没有，可设默认值
        created_at=int(time.time()),
        deadline=order_data.end_time,
        item_image=str(order_data.sth_image)  # 如果是列表存字符串
    )

    # 保存到数据库
    try:
        session.add(new_order)
        session.commit()
        session.refresh(new_order)
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail= f" 失败{str(e)}")
    return {"message":"创建成功"}
