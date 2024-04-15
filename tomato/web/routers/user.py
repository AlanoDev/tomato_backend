from fastapi import APIRouter
from tomato.repository.dao.user_dao import UserDao
from tomato.repository.user import UserRepository
from tomato.service.user import UserService
from tomato.domain import User as UserDomain
from pydantic import BaseModel
router = APIRouter(prefix='/user')
ud = UserDao()
ur = UserRepository(ud)
us = UserService(ur)


class User(BaseModel):
    name: str | None
    email: str | None
    password: str | None


@router.post("/signup")
def signup(user: User):
    ret=us.signup(user)
    code=ret
    return {
        "code": code,
        "msg": "注册成功" if code>=0 else "用户名或邮箱已存在",
        "data": {
            "id": ret if code>=0 else -1
        }
    }


@router.post("/login")
def login(name: str, password: str):
    ret=us.login(name, password)
    code=ret
    return {
        "code": code,
        "msg": "登录成功" if code>0 else "用户名或密码错误",
        "data": {
            "id": ret if code>0 else -1
        }
    }

roles=['admin','user','guest']
@router.put("/role/{:id}")
def set_role(id: int, role: str):
    domain = us.get_by_id(id)
    if domain is not None:
        if role in roles:
            domain.role = role
            us.update(domain)
            return {'code': 0, }
        else:
            return "非法角色！"
           
    return {'code': -1,"msg": "用户不存在"}


@router.put("/{:id}")
def update(id: int, user: User):
    domain = UserDomain(name=user.name, email=user.email,
                        password=user.password, id=id)
    ret = us.update(domain)
    code = ret
    return {
        "code": code,
        "msg": "更新成功" if code>=0 else "用户不存在",
    }

@router.delete("/{:id}")
def delete(id: int):
    ret = us.delete(id)
    code = ret
    return {
        "code": code,
        "msg": "删除成功" if code>=0 else "用户不存在",
    }
