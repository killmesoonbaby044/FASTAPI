from fastapi import FastAPI

from app.routers import users, post, auth, vote, random
from fastapi.middleware.cors import CORSMiddleware
from .utils import database_check
# from database import engine
# import models
# creating non-existing base
# models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="KILLMESOONBABY044")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(post.router)
app.include_router(auth.router)
app.include_router(vote.router)
app.include_router(random.router)


@app.get('/')
def hello():
    return {'message': 'hello people i have finished'}


@app.on_event("startup")
def db_test():
    database_check()
