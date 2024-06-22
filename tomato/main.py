from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from tomato.web.routers.user import router as user
from tomato.web.routers.article import router as article
from tomato.web.routers.history import router as history
from tomato.web.routers.file import router as file
from tomato.web.routers.favorite import router as favorite
from tomato.web.routers.disease import router as disease
from tomato.repository.model import database_migrate
from fastapi.middleware.cors import CORSMiddleware
database_migrate()

app = FastAPI()  # 默认localhost的地址，端口8000


# 进行跨越处理，因为跨越问题是普遍存在的，所以fastapi提供了解决的方案，使用了fastapi自己的提供的跨域中间件进行了处理
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 提供静态文件的服务，使用fastapi框架自己提供的，显示图片，可以在浏览器输入地址进行访问
app.mount("/static", StaticFiles(directory="./tomato/files"), name="files")

# 注册路由
app.include_router(user)
app.include_router(article)
app.include_router(history)
app.include_router(file)
app.include_router(favorite)
app.include_router(disease)
