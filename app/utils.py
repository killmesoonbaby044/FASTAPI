from passlib.context import CryptContext

from app.database import engine

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hashing(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def database_check():
    try:
        answer = engine.execute("SELECT 1").fetchall()
        if str(answer) == '[(1,)]':
            print("DATABASE CONNECTED")
    except Exception:
        print("Connection error")
        raise
