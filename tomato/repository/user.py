from tomato.repository.dao.user_dao import IUserDao
from tomato.domain import User
import abc


class IUserRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(self, user: User) -> int:
        pass

    @abc.abstractmethod
    def get_by_name(self, name: str) -> User | None:
        pass

    @abc.abstractmethod
    def get_by_email(self, email: str) -> User | None:
        pass

    @abc.abstractmethod
    def get_by_id(self, id: int) -> User | None:
        pass

    @abc.abstractmethod
    def delete(self, id: int) -> int:
        pass

    @abc.abstractmethod
    def update(self, user: User) -> int:
        pass


class UserRepository():
    def __init__(self, dao: IUserDao):
        self.dao: IUserDao = dao

    def create(self, user: User) -> int:
        return self.dao.create(user)

    def get_by_name(self, name: str) -> User | None:
        return self.dao.get_by_name(name)

    def get_by_email(self, email: str) -> User | None:
        return self.dao.get_by_email(email)

    def get_by_id(self, id: int) -> User | None:
        return self.dao.get_by_id(id)

    def delete(self, id: int) -> int:
        return self.dao.delete(id)

    def update(self, user: User) -> int:
        return self.dao.update(user)
