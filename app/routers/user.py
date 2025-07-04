from fastapi import  status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users", #it is prefix of the route path of users like http://127.0.0.1:8000/users
    tags = ['Users'] #to categorize, identify, and organize APIs and their resources
)

@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate, db: Session = Depends(get_db)):

    ##hash the password - userpassword
    hashed_password =  utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict()) ## (** are unpacking the dictionary)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id: {id} does not exist')
    return user