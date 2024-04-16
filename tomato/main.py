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

app = FastAPI()

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

app.mount("/static", StaticFiles(directory="./tomato/files"), name="files")

app.include_router(user)
app.include_router(article)
app.include_router(history)
app.include_router(file)
app.include_router(favorite)
app.include_router(disease)
