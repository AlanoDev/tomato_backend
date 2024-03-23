from fastapi import FastAPI
from tomato.web.routers.user import router as user
from tomato.web.routers.article import router as article
from tomato.web.routers.history import router as history
from tomato.web.routers.upload import router as upload
app = FastAPI()
app.include_router(user)
app.include_router(article)
app.include_router(history)
app.include_router(upload)
