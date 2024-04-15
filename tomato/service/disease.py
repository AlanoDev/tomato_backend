from tomato.domain import Disease
from tomato.repository.disease import IDiseaseRepository


class DiseaseService():
    def __init__(self, disease_repository: IDiseaseRepository) -> None:
        self.disease_repository: IDiseaseRepository = disease_repository

    def get_by_title(self, title: str) -> Disease | None:
        return self.disease_repository.get_by_title(title)

    def get_all(self) -> list[Disease]:
        return self.disease_repository.get_all()

    def get_by_id(self, id: int) -> Disease | None:
        return self.disease_repository.get_by_id(id)

    def create(self, disease: Disease) -> int:
        return self.disease_repository.create(disease)

    def update(self, disease: Disease) -> int:
        return self.disease_repository.update(disease)


    def delete(self, id: int) -> int:
        if self.get_by_id(id) is None:
            return -1
        return self.disease_repository.delete(id)
