from datetime import datetime
from fastapi import APIRouter, UploadFile
from pydantic import BaseModel
from tomato.domain import Disease
from tomato.repository.disease import DiseaseRepository
from tomato.repository.dao.disease_dao import DiseaseDao
from tomato.service.disease import DiseaseService
from pathlib import Path, WindowsPath
import requests

router = APIRouter(prefix='/disease')

dd = DiseaseDao()
dr = DiseaseRepository(dd)
ds = DiseaseService(dr)


class Disease(BaseModel):
    tittle: str
    description: str
    healing: str
    prevention: str


@router.get('/')
async def get_by_tittle(tittle: str):
    return ds.get_by_tittle(tittle)


@router.get('/:id')
async def get_by_id(id: int):
    return ds.get_by_id(id)


@router.get('/all')
async def get_all():
    return ds.get_all()


@router.post('/')
async def create(disease: Disease):
    domain = Disease(tittle=disease.tittle, description=disease.description,
                     healing=disease.healing, prevention=disease.prevention)
    return ds.create(domain)


@router.post('/recognition')
async def upload(file: UploadFile, user_id: int):
    if file.content_type.split('/')[0] != 'image':
        return -1
    now = datetime.now().timestamp()
    file_name = f'{user_id}'+'_' + \
        f'{now}.'+file.content_type.split('/')[1]
    path = r'./files/'+file_name
    path = Path.joinpath(Path.cwd(), 'files', file_name)
    with open(path, 'wb') as buffer:
        buffer.write(file.file.read())
    res = requests.get('http://127.0.0.1:8100?image='+str(WindowsPath(path)))
    result =str(res._content, encoding='utf-8').split('\n')[0].split(' ')
    result = ' '.join(result[1:])
    return result


@router.put('/')
async def update(disease: Disease):
    domain = Disease(id=disease.id, tittle=disease.tittle, description=disease.description,
                     healing=disease.healing, prevention=disease.prevention)
    return ds.update(domain)


@router.delete('/')
async def delete(id: int):
    return ds.delete(id)
