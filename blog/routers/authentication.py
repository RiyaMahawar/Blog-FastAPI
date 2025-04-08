from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models
from ..hashing import Hash
from sqlalchemy.orm import Session
from ..JWTtoken import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=["login"])

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Invalid Credentials")
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token" : access_token , "token_type" : "bearer"}



#POSTMAN:
#POST URL: :8000/LOGIN
#BODY FORM-DATA: KEY: riya@gmail.com, PASSWORD: password
#OUTPUT: {
#     "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJyaXlhQGdtYWlsLmNvbSIsImV4cCI6MTc0NDAyMTQ4MX0.An1X1NT7iu1x5TDoNkNxy7OFaAZkuHxR1oPPbfDwM0M",
#     "token_type": "bearer"
# }


#GET URL: 8000/blog
#HEADER: KEY: Authorization, VALUE: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJyaXlhQGdtYWlsLmNvbSIsImV4cCI6MTc0NDAyMTE4M30._q1JwaR7oFZcbP-APWrW8ojiC2CHeSONl6jrpCCD-KM
#OUTPUT: [
#     {
#         "title": "second blog",
#         "body": "body of blog",
#         "creator": {
#             "name": "riya",
#             "email": "riya@gmail.com",
#             "blogs": [
#                 {
#                     "title": "second blog",
#                     "body": "body of blog"
#                 },
#                 {
#                     "title": "hello",
#                     "body": "string"
#                 },
#                 {
#                     "title": "str",
#                     "body": "st"
#                 }
#             ]
#         }
#     },
#     {
#         "title": "hello",
#         "body": "string",
#         "creator": {
#             "name": "riya",
#             "email": "riya@gmail.com",
#             "blogs": [
#                 {
#                     "title": "second blog",
#                     "body": "body of blog"
#                 },
#                 {
#                     "title": "hello",
#                     "body": "string"
#                 },
#                 {
#                     "title": "str",
#                     "body": "st"
#                 }
#             ]
#         }
#     },
#     {
#         "title": "str",
#         "body": "st",
#         "creator": {
#             "name": "riya",
#             "email": "riya@gmail.com",
#             "blogs": [
#                 {
#                     "title": "second blog",
#                     "body": "body of blog"
#                 },
#                 {
#                     "title": "hello",
#                     "body": "string"
#                 },
#                 {
#                     "title": "str",
#                     "body": "st"
#                 }
#             ]
#         }
#     }
# ]