from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session 
from typing import List
from ..repository import blogrepo

get_db = database.get_db

router = APIRouter(prefix='/blog',
                   tags=['blogs'])

@router.get('/', response_model = List[schemas.ShowBlog])
def all_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogrepo.all_blogs(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request : schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogrepo.create_blog(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogrepo.destroy(id,db)


@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogrepo.update(id,request,db)


@router.get('/{id}', status_code=200, response_model = schemas.ShowBlog)
def show(id:int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogrepo.show(id,db)