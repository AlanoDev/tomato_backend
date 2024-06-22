from fastapi import APIRouter
from tomato.repository.dao.article_dao import ArticleDao
from tomato.repository.article import ArticleRepository
from tomato.repository.dao.disease_dao import DiseaseDao
from tomato.repository.disease import DiseaseRepository
from tomato.service.article import ArticleService
from tomato.repository.dao.user_dao import UserDao
from tomato.repository.user import UserRepository
from tomato.domain import Article as ArticleDomain
from tomato.web.utils.results import handle_results
from pydantic import BaseModel

router = APIRouter(prefix='/article')

ad = ArticleDao()
ud = UserDao()
ur = UserRepository(ud)
ar = ArticleRepository(ad)
dd = DiseaseDao()
dr = DiseaseRepository(dd)

asv = ArticleService(ar, ur, dr)


class Article(BaseModel):
    id: int | None = None
    title: str
    content: str
    image: str | None
    disease: int



@router.get('/all')
async def get_all_articles():
    res = asv.get_all_articles()
    res_list: list[Article] = []
    for item in res:
        res_list.append(Article(id=item.id, title=item.title,
                        content=item.content, image=item.image, disease=item.disease))
    return handle_results(False, 'Success', res_list, 0)   # 统一处理返回格式


@router.get('/disease/{id}')
async def get_by_disease_id(id: int):
    res = asv.get_by_disease(id)
    res_list: list[Article] = []
    for item in res:
        res_list.append(Article(id=item.id, title=item.title,
                        content=item.content, image=item.image, disease=item.disease))
    return handle_results(False, 'Success', res_list, 0)


@router.get('/{id}')
async def get_by_id(id: int):
    res = asv.get_by_id(id)
    if res is None:
        return handle_results(True, '', None, 10+1)
    ret = Article(id=res.id, title=res.title, content=res.content,
                  image=res.image, disease=res.disease)
    return handle_results(False, 'Success', ret, 0)


@router.get('/{title}')
async def get_by_title(title: str):
    res = asv.get_by_title(title)
    if res is None:
        return handle_results(True, '', None, 10+1)
    ret = Article(id=res.id, title=res.title, content=res.content,
                  image=res.image, disease=res.disease)
    return handle_results(False, 'Success', ret, 0)


@router.post('/')
async def create(article: Article):
    print(article)
    domain = ArticleDomain(title=article.title, content=article.content,
                           image=article.image, disease=article.disease)
    ret = asv.create(domain)
    if ret == -1:
        return handle_results(True, '', None, 10+3)
    return handle_results(False, 'Success', {"id":ret}, 0)


@router.put('/{id}')
async def update(article: Article, id: int):
    print(article.content)
    domain = ArticleDomain(id=id, title=article.title,
                           content=article.content, image=article.image, disease=article.disease)
    if asv.update(domain) == -1:
        return handle_results(True, '', None, 10+4)
    return handle_results(False, 'Success', None, 0)


@router.delete('/{id}')
async def delete(id: int):
    if asv.delete(id) == -1:
        return handle_results(True, '', None, 10+5)
    return handle_results(False, 'Success', None, 0)
