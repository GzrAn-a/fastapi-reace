from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.src.db import get_session
from app.src.schemas.response.schemas_order.schemas_order_index import SchemaOrderIndex
from app.src.models.ModelProject import ModelProject
from app.src.models.ModelUser import ModelUser

router = APIRouter()


@router.get('/index', response_model=list[SchemaOrderIndex], summary="小程序首页抢单")
async def api_get_order(session: Session = Depends(get_session)):
    """Get the order 获取订单"""


    # 应该要从用户 token JWT等中获得用户的 id 来查询用户的 school_id 是否为 0，若为 0 则审核不通过
    # all_users = session.exec(select(ModelUser).where(ModelUser.school_id != 0)).first()
    # # if all_users is None:
    # #     return all_users
    # #     return {"message":"学校信息未通过审核"}
    # # 使用 join 关联查询，一次性获取订单和对应的用户数据
    all_projects = session.exec(select(ModelProject)).all()
    print(f"数据库中总共有 {len(all_projects)} 条订单")

    for i in all_projects:
        print("数据条数",i)




    statement = (
        select(ModelProject, ModelUser)
        .outerjoin(ModelUser, ModelProject.publisher_openid == ModelUser.openid)
        .where(ModelProject.status == 0 , ModelUser.school_id != 0) # shcool_id == 代表未通过管理员审核，不能查询和使用
    )

    results = session.exec(statement).all()

    print("results:", results)
    order_list = []
    for project, user in results:
        # 将数据库模型转换为 Schema
        order_dto = SchemaOrderIndex(
            order_id=project.id,
            user_id=user.id,
            # 必须使用模型中定义的正确属性名
            avatar=user.avatar_url if user.avatar_url else "",
            user_name=user.nick_name,
            from_address=project.from_address,
            to_address=project.to_address,
            start_time=project.created_at,
            end_time=project.deadline,
            money=project.price,
            status=project.status,
            distance=0
        )
        order_list.append(order_dto)
    return order_list
