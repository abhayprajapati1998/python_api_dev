from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional
from typing_extensions import Annotated
from pydantic import conint

class PostBase(BaseModel): #this is pydantic model or schema (it defines the structure of a request and response) i.e what a user request and what it get a response
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel): #this schema is the response we give, when a user is created. So the data we get came from database,
    # which is a sqlalchemy or orm model, so we need to convert the orm objet to dict or json
    id: int
    email: EmailStr
    created_at: datetime

    class config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    #this will help converting the to sqlalchemy model(orm object) to pydantic model(json or dict)
    
    class config: 
        orm_mode = True

class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    class config: #this will help converting the to sqlalchemy model(orm object) to pydantic model(json or dict)
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    # dir: conint(strict= True, le=1)
    dir: Annotated[int, Field(strict=True, le=1)]
