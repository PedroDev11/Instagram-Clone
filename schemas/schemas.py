from pydantic import BaseModel
from datetime import datetime
from typing import List

# We request this
class UserBase(BaseModel):
    username: str
    email: str
    password: str

# We return this
class UserDisplay(BaseModel):
    username: str
    email: str

# FOR POSTDISPLAY
class User(BaseModel):
    username: str
    
# FOR POSTDISPLAY
class Comment(BaseModel):
    text: str
    username: str
    timestamp: datetime

# we need the base class to send information to our API and we´re going to need the display class
# as well to receive information from the API
class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int
    
class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    comments: List[Comment]
    
class UserAuth(BaseModel):
    id: int
    username: str
    email: str
    
class CommentBase(BaseModel):
    username: str
    text: str
    post_id: int