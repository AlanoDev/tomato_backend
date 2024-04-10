import uvicorn  
from tomato.main import app;

if __name__ == "__main__":
    uvicorn.run(app=app,reload=True)