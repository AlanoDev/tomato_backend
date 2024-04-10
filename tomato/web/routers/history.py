from fastapi import APIRouter
from tomato.domain import History
from tomato.repository.history import HistoryRepository
from tomato.repository.dao.history_dao import HistoryDao
from tomato.service.history import HistoryService
router = APIRouter(prefix='/history')

hd = HistoryDao()
hr = HistoryRepository(hd)
hs = HistoryService(hr)

@router.get('/')
async def get_all_history(user_id: int):
    return hs.get_by_user(user_id)

@router.delete('/')
async def delete_history(id: int):
    return hs.delete(id)

@router.post('/')
async def create_history(user_id: int, article_id: int):
    domain = History(user_id=user_id, article_id=article_id)
    return hs.create(domain)