from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from app import models, schemas, oauth2
from app.database import get_db

router = APIRouter(
    prefix='/posts',
    tags=['Post']
)


# @router.get('', response_model=List[schemas.Post])
@router.get('/', response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), current_user=Depends(oauth2.get_current_user),
              search: Optional[str] = "", skip: int = 0, limit: int = 10):
    # posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()
    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).offset(skip).limit(limit).all()
    posts = db.query(
        models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(
        models.Post.title.contains(search)).offset(skip).limit(limit).all()
    return posts


@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id: int, db: Session = Depends(get_db), current_user=Depends(oauth2.get_current_user)):
    one_post = db.query(
        models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(
        models.Post.id).filter(models.Post.id == id).first()
    # one_post = db.query(
    #     models.Post, func.count(models.Vote.post_id).label("votes")).join(
    #     models.Vote, isouter=True).group_by(
    #     models.Post.id).filter(models.Post.id == id).first()
    if not one_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")

    # if one_post.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
    #                         detail="NO PERMISSION FOR THIS POST!!!")

    return one_post


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db),
                 current_user=Depends(oauth2.get_current_user)):

    new_post = models.Post(owner_id=current_user.id,  **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
@router.delete("/{id}")
def delete_post(id: int, db: Session = Depends(get_db), current_user=Depends(oauth2.get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} not exists")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="NO PERMISSION FOR THIS POST!!!")

    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db),
                current_user=Depends(oauth2.get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} not exists")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="NO PERMISSION FOR THIS POST!!!")

    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
