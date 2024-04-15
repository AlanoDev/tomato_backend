from tomato.repository.dao.disease_dao import IDiseaseDao
from tomato.domain import Disease
import abc


class IDiseaseRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_by_title(self, title: str) -> Disease | None:
        pass

    @abc.abstractmethod
    def get_by_id(self, id: int) -> Disease | None:
        pass

    @abc.abstractmethod
    def get_all(self) -> list[Disease]:
        pass

    @abc.abstractmethod
    def create(self, disease: Disease) -> int:
        pass

    @abc.abstractmethod
    def update(self, disease: Disease) -> int:
        pass

    @abc.abstractmethod
    def delete(self, id: int) -> int:
        pass


class DiseaseRepository(IDiseaseRepository):
    def __init__(self, dao: IDiseaseDao) -> None:
        self.dao: IDiseaseDao = dao

    def get_all(self) -> list[Disease]:
        return self.dao.get_all()

    def get_by_title(self, title: str) -> Disease | None:
        return self.dao.get_by_title(title)

    def get_by_id(self, id: int) -> Disease | None:
        return self.dao.get_by_id(id)

    def create(self, disease: Disease) -> int:
        return self.dao.create(disease)

    def update(self, disease: Disease) -> int:
        return self.dao.update(disease)

    def delete(self, id: int) -> int:
        return self.dao.delete(id)
