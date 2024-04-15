from datetime import datetime
from fastapi import APIRouter, UploadFile
from pydantic import BaseModel
from tomato.domain import Disease as DiseaseDomain
from tomato.repository.disease import DiseaseRepository
from tomato.repository.dao.disease_dao import DiseaseDao
from tomato.service.disease import DiseaseService
from pathlib import Path, WindowsPath
from tomato.web.utils.results import handle_results
import requests

router = APIRouter(prefix='/disease')

dd = DiseaseDao()
dr = DiseaseRepository(dd)
ds = DiseaseService(dr)


class Disease(BaseModel):
    id: int | None = None
    title: str
    description: str
    healing: str
    prevention: str


@router.get('/')
async def get_by_title(title: str):
    res = ds.get_by_title(title)
    if res is None:
        return handle_results(True, '', None, 50+1)
    ret = Disease(id=res.id, title=res.title, description=res.description,
                  healing=res.healing, prevention=res.prevention)
    return handle_results(False, 'Success', ret, 0)


@router.get('/:id')
async def get_by_id(id: int):
    res = ds.get_by_id(id)
    if res is None:
        return handle_results(True, '', None, 50+1)
    ret = Disease(id=res.id, title=res.title, description=res.description,
                  healing=res.healing, prevention=res.prevention)
    return handle_results(False, 'Success', ret, 0)


@router.get('/all')
async def get_all():
    res = ds.get_all()
    res_list: list[Disease] = []
    for item in res:
        res_list.append(Disease(id=item.id, title=item.title, description=item.description,
                        healing=item.healing, prevention=item.prevention))
    return handle_results(False, 'Success', res_list, 0)


@router.post('/')
async def create(disease: Disease):
    domain = Disease(title=disease.title, description=disease.description,
                     healing=disease.healing, prevention=disease.prevention)
    if ds.create(domain) == -1:
        return handle_results(True, '', None, 50+3)
    return handle_results(False, 'Success', None, 0)


@router.post('/recognition')
async def upload(file: UploadFile):
    if file.content_type.split('/')[0] != 'image':
        return -1
    now = datetime.now().timestamp()
    file_name = 'disease_' + f'{now}.'+file.content_type.split('/')[1]
    path = r'./files/'+file_name
    path = Path.joinpath(Path.cwd(), 'tomato', 'files', file_name)
    with open(path, 'wb') as buffer:
        buffer.write(file.file.read())
    res = requests.get('http://127.0.0.1:8100?image='+str(WindowsPath(path)))
    result = str(res._content, encoding='utf-8').split('\n')[0].split(' ')
    result = ' '.join(result[1:])
    ds.create(Disease(title=result, description='description',
                      healing='healing', prevention='prevention'))
    return handle_results(False, 'Success', {"disease": result, 'link': r'http://127.0.0.1:8000/static/'+file_name}, 0)


@ router.put('/:id')
async def update(disease: Disease, id: int):
    domain = DiseaseDomain(id=id, title=disease.title, description=disease.description,
                           healing=disease.healing, prevention=disease.prevention)
    if ds.update(domain) == -1:
        return handle_results(True, '', None, 50+4)
    return handle_results(False, 'Success', None, 0)


@ router.delete('/')
async def delete(id: int):
    if ds.delete(id) == -1:
        return handle_results(True, '', None, 50+5)
    return handle_results(False, 'Success', None, 0)
