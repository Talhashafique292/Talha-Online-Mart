from fastapi import APIRouter, Depends
from typing import Annotated
from app.controllers.crud_user import user_add
from app.models.user_models import UserModel

router = APIRout()

@router.get("/user")
def get_user():
    ...

@router.post('./add_user')
def add_users(user: Annotated[UserModel, Depends(user_add)]):
    return user 

@router.put('./update_user')
def update_users():
    ...   

@router.delete('./delete_user') 
def delete_user():
    ...   
