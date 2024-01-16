from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from database.connection import get_db
from database.db_comment import getAllComments, createComment
from auth.oauth2 import get_current_user
from schemas.schemas import CommentBase, UserAuth

router = APIRouter(
    prefix='/comment',
    tags=['API comment']
)

@router.get('/all/{post_id}')
def get_all(post_id: int, db: Session = Depends(get_db)):
    return getAllComments(post_id, db)

@router.post('')
def create_comment(request: CommentBase, db: Session = Depends(get_db), curent_user: UserAuth = Depends(get_current_user)):
    return createComment(request, db)