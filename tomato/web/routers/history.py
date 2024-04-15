from fastapi import APIRouter
from pydantic import BaseModel
from tomato.domain import History
from tomato.repository.article import ArticleRepository
from tomato.repository.dao.article_dao import ArticleDao
from tomato.repository.dao.user_dao import UserDao
from tomato.repository.history import HistoryRepository
from tomato.repository.dao.history_dao import HistoryDao
from tomato.repository.user import UserRepository
from tomato.service.history import HistoryService
from tomato.web.utils.results import handle_results
router = APIRouter(prefix='/history')

hd = HistoryDao()
hr = HistoryRepository(hd)
ud= UserDao()
ur= UserRepository(ud)
ad= ArticleDao()
ar= ArticleRepository(ad)
hs = HistoryService(hr, ur, ar)



class History(BaseModel):
    user_id: int
    article_id: int


@router.get('/')
async def get_all_history(user_id: int):
    res = hs.get_by_user(user_id)
    res_list: list[History] = []
    for item in res:
        res_list.append(
            History(id=item.id, user_id=item.user_id, article_id=item.article_id))
    return handle_results(False, 'Success', res_list, 0)


@router.delete('/')
async def delete_history(id: int):
    if hs.delete(id) == -1:
        return handle_results(True, '', None, 30+2)
    return handle_results(False, 'Success', None, 0)


@router.post('/')
async def create_history(user_id: int, article_id: int):
    domain = History(user_id=user_id, article_id=article_id)
    if hs.create(domain) == -1:
        return handle_results(True, '', None, 30+1)
    else:
        return handle_results(False, 'Success', None, 0)
