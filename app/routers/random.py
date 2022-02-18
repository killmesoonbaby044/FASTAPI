from fastapi import status, APIRouter
from fastapi.responses import RedirectResponse


router = APIRouter(
    prefix='/random',
    tags=['TESTING']
)


@router.get("/1")
def redirect_typer():
    return RedirectResponse("/")


@router.get("/2", response_class=RedirectResponse, status_code=status.HTTP_307_TEMPORARY_REDIRECT)
def redirect_fastapi():
    return
