from sqlalchemy.orm.session import Session
from .models import DBComment
from schemas.schemas import CommentBase
import datetime

def createComment(request: CommentBase, db: Session):
    new_comment = DBComment(
        text = request.text,
        username = request.username,
        post_id = request.post_id,
        timestamp = datetime.datetime.now()
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def getAllComments(post_id: int, db: Session):
    return db.query(DBComment).filter(DBComment.post_id == post_id).all()