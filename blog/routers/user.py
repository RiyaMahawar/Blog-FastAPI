from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session 
# from ..hashing import Hash
from ..repository import userrepo

get_db = database.get_db

router = APIRouter(prefix = '/user',
                   tags=['users']
                   )

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return userrepo.create_user(request,db)


@router.get('/{id}',response_model= schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    return userrepo.get_user(id,db)