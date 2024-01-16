from sqlalchemy.orm.session import Session
from schemas.schemas import PostBase
from database.models import DBPost
import datetime
from fastapi import HTTPException, status

def create_post(request: PostBase, db: Session):
    new_post = DBPost(
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        caption = request.caption,
        timestamp = datetime.datetime.now(),
        user_id = request.creator_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def getPosts(db: Session):
    return db.query(DBPost).all()

def deletePost(id: int, user_id: int, db: Session):
    post = db.query(DBPost).filter(DBPost.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")
    if post.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Only post creator can delete post")
    db.delete(post)
    db.commit()
    return "ok"