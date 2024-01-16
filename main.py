# py -m venv env
# .\env\Scripts\activate.bat
# py -m uvicorn main:app --reload
# py -m pip install -r requirements.txt
from fastapi import FastAPI
from database import models
from routers import user, post, comment
from database.connection import engine
from fastapi.staticfiles import StaticFiles
from auth import authentication
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(authentication.router)

@app.get('/')
def home():
    return {"message": "Hello world!"}

models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ['*']
)