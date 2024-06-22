import abc
from tomato.repository.model import DiseaseModel
from tomato.domain import Disease
import datetime


class IDiseaseDao(metaclass=abc.ABCMeta):
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


class DiseaseDao(IDiseaseDao):

    def get_all(self) -> list[Disease]:
        return list(DiseaseModel.select())

    def get_by_title(self, title: str) -> Disease | None:
        return DiseaseModel.get_or_none(DiseaseModel.title == title)

    def get_by_id(self, id: int) -> Disease | None:
        return DiseaseModel.get_or_none(DiseaseModel.id == id)

    def create(self, disease: Disease) -> int:
        try:
            ret = DiseaseModel.create(title=disease.title, description=disease.description,
                                      prevention=disease.prevention, healing=disease.healing, created_date=datetime.datetime.now())
            return ret.id
        except:
            return -1

    def update(self, disease: Disease) -> int:
        cdi = self.get_by_id(disease.id)
        if cdi is not None:
            cdi.title = disease.title if len(
                disease.title) != 0 else cdi.title
            cdi.description = disease.description if len(
                disease.description) != 0 else cdi.description
            cdi.prevention = disease.prevention if len(
                disease.prevention) != 0 else cdi.prevention
            cdi.healing = disease.healing if len(
                disease.healing) != 0 else cdi.healing
            cdi.updated_date = datetime.datetime.now()
            cdi.save()
            return 0
        return -1

    def delete(self, id: int) -> int:
        try:
            DiseaseModel.delete_by_id(id)
            return 0
        except:
            return -1
