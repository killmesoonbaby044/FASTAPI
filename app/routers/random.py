from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from fastapi.responses import RedirectResponse


from app import models, schemas, oauth2
from app.database import get_db

router = APIRouter(
    prefix='/random',
    tags=['TESTING']
)


@router.get("/1")
def redirect_typer():
    return RedirectResponse("/")


@router.get("/2", response_class=RedirectResponse)
async def redirect_fastapi():
    return "/"
