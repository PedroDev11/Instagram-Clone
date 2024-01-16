from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from schemas.schemas import UserBase
from database.models import DBUser
from common.hash import Hash

# we have a model (DBUser). so what we need to do is we need to convert from request into our DBUser
def createUser(request: UserBase, db: Session):
    new_user = DBUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_username(db: Session, username: str):
    user = db.query(DBUser).filter(DBUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Username: {username} not found")
    return user