from tomato.repository.user import IUserRepository
from tomato.domain import User
import base64


class UserService():
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def signup(self, user: User) -> int:
        if user.name is None or user.email is None or user.password is None:
            return -3
        if self.repository.get_by_email(user.email) is not None or self.repository.get_by_name(user.name) is not None:
            return -2
        return self.repository.create(user)

    def login(self, name: str, password: str) -> int:
        if self.repository.get_by_name(name) is None:
            return -1
        if self.repository.get_by_name(name).password != password:
            return -2
        return self.repository.get_by_name(name).id

    def update(self, user: User) -> int:
        return self.repository.update(user)

    def delete(self, id: int) -> int:
        return self.repository.delete(id)

    def get_by_id(self, id: int) -> User | None:
        return self.repository.get_by_id(id)
