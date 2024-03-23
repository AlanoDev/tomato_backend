import abc
from tomato.repository.model import UserModel
from tomato.domain import User
import datetime


class IUserDao(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create(self, user: User) -> int:
        pass

    @abc.abstractmethod
    def get_by_name(self, name: str) -> User | None:
        pass

    @abc.abstractmethod
    def get_by_id(self, id: int) -> User | None:
        pass

    @abc.abstractmethod
    def get_by_email(self, email: str) -> User | None:
        pass

    @abc.abstractmethod
    def update(self, user: User):
        pass

    @abc.abstractmethod
    def delete(self, id: int):
        pass


class UserDao(IUserDao):

    def create(self, user: User) -> int:
        return UserModel.create(name=user.name, email=user.email,
                                password=user.password, role='user').id

    def get_by_name(self, name: str) -> User | None:
        user = UserModel.get_or_none(UserModel.name == name)
        return user

    def get_by_id(self, id: int) -> User | None:
        user = UserModel.get_or_none(UserModel.id == id)
        return user

    def get_by_email(self, email: str) -> User | None:
        user = UserModel.get_or_none(UserModel.email == email)
        return user

    def delete(self, id: int):
        UserModel.delete_by_id(id)

    def update(self, user: User):
        cu: UserModel = UserModel.get_by_id(user.id)
        cu.name = user.name if user.name is not None else cu.name
        cu.email = user.email if user.email is not None else cu.email
        cu.role = user.role if user.role is not None else cu.role
        cu.password = user.password if user.password is not None  else cu.password
        cu.updated_date = datetime.datetime.now()
        cu.save()
