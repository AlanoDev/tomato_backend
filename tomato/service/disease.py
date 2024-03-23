from tomato.domain import Disease
from tomato.repository.disease import IDiseaseRepository


class DiseaseService():
    def __init__(self, disease_repository: IDiseaseRepository) -> None:
        self.disease_repository: IDiseaseRepository = disease_repository

    def get_by_tittle(self, tittle: str) -> Disease:
        return self.disease_repository.get_by_tittle(tittle)

    def create(self, disease: Disease) -> int:
        if self.disease_repository.get_by_tittle(disease.tittle) is not None:
            return -1
        self.disease_repository.create(disease)
        return 0
    def update(self, disease: Disease):
        self.disease_repository.update(disease)

    def delete(self, id: int):
        self.disease_repository.delete(id)
