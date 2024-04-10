from tomato.repository.dao.disease_dao import IDiseaseDao
from tomato.domain import Disease
import abc


class IDiseaseRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_by_tittle(self, tittle: str) -> Disease:
        pass

    @abc.abstractmethod
    def create(self, disease: Disease) -> int:
        pass

    @abc.abstractmethod
    def update(self, disease: Disease):
        pass

    @abc.abstractmethod
    def delete(self, id: int):
        pass


class DiseaseRepository(IDiseaseRepository):
    def __init__(self, dao: IDiseaseDao) -> None:
        self.dao: IDiseaseDao = dao

    def    get_all(self) -> list[Disease]:
        return self.dao.get_all()

    def get_by_tittle(self, tittle: str) -> Disease:
        return self.dao.get_by_tittle(tittle)
    
    def get_by_id(self, id: int) -> Disease:
        return self.dao.get_by_id(id)

    def create(self, disease: Disease) -> int:
        return self.dao.create(disease)

    def update(self, disease: Disease):
        self.dao.update(disease)

    def delete(self, id: int):
        self.dao.delete(id)
