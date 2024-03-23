import abc
from tomato.repository.model import DiseaseModel
from tomato.domain import Disease
import datetime

class IDiseaseDao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_by_tittle(self, tittle: str) -> Disease:
        pass

    @abc.abstractmethod
    def create(self, disease: Disease) -> id:
        pass

    @abc.abstractmethod
    def update(self, disease: Disease):
        pass

    @abc.abstractmethod
    def delete(self, id: int):
        pass


class DiseaseDao(IDiseaseDao):
    def get_by_tittle(self, tittle: str) -> Disease:
        return DiseaseModel.get(DiseaseModel.tittle == tittle)

    def create(self, disease: Disease) -> id:
        return DiseaseModel.create(tittle=disease.tittle, introduction=disease.introduction,
                                   prevention=disease.prevention, healing=disease.healing).id

    def update(self, disease: Disease):
        cdi: DiseaseModel = DiseaseModel.get_by_id(disease.id)
        cdi.tittle=disease.tittle if len(disease.tittle)!=0 else cdi.tittle
        cdi.introduction=disease.introduction if len(disease.introduction)!=0 else cdi.introduction
        cdi.prevention=disease.prevention if len(disease.introduction)!=0 else cdi.prevention
        cdi.healing=disease.healing if len(disease.healing)!=0 else cdi.healing
        cdi.updated_date=datetime.datetime.now()
        cdi.save()
    def delete(self, id: int):
        DiseaseModel.delete_by_id(id)
