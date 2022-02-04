from fastapi import FastAPI
from app.routers import users, post, auth, vote
from fastapi.middleware.cors import CORSMiddleware
# from database import engine
# import models
# creating non-existing base
# models.Base.metadata.create_all(bind=engine)


app = FastAPI()

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


@app.get('/')
def hello():
    return {'message': 'hello people i have finished'}
