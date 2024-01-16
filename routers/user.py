from fastapi import APIRouter, Depends
from schemas.schemas import UserDisplay, UserBase
from sqlalchemy.orm.session import Session
from database.db_user import createUser
from database.connection import get_db

router = APIRouter(
    prefix='/user',
    tags=['API user']
)

# we have a response model that´s going to be UserDisplay, so i want to have my user display returned, not the 
# actual information that´s returned from the database
@router.post('/create', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return createUser(request, db)