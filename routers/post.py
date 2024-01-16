from fastapi import APIRouter, Depends, status, HTTPException, UploadFile, File
from schemas.schemas import PostBase, PostDisplay, UserAuth
from sqlalchemy.orm.session import Session
from database.connection import get_db
from database.db_post import create_post, getPosts, deletePost
from auth.oauth2 import get_current_user
import random
import string
import shutil
from typing import List

router = APIRouter(
    prefix='/post',
    tags=['API post']
)

image_url_type = ['absolute', 'relative']

@router.post('', response_model=PostDisplay)
def create(request: PostBase, db: Session = Depends(get_db), curent_user: UserAuth = Depends(get_current_user)):
    if not request.image_url_type in image_url_type:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
                            detail="Parameter image_url_type can only take values 'absolute' or 'relative'.")
    return create_post(request, db)

@router.get('/all', response_model=List[PostDisplay]) # response_model=List[PostDisplay]
def getAll(db: Session = Depends(get_db)):
    return getPosts(db)

@router.post('/image')
def uploadImage(image: UploadFile = File(...), curent_user: UserAuth = Depends(get_current_user)):
    letter = string.ascii_letters
    rand_str = ''.join(random.choice(letter) for ii in range(6))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'
    
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)
        
    return {
        'filename': path
    }
    
@router.delete('/delete/{id}')
def delete_post(id: int, db: Session = Depends(get_db), curent_user: UserAuth = Depends(get_current_user)):
    return deletePost(id, curent_user.id, db)