from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.routers.users.model.userMd import UserValidator
from app.routers.users.schema.userDb import User
from app.db.database import get_db

router = APIRouter()

@router.get("/users",response_model=list[UserValidator])
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.post("/user/create", response_model=UserValidator)
def create_user(user: UserValidator, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.put("/user/edit/{user_id}", response_model=UserValidator)
def edit_user(user_id: int, user: UserValidator, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user is None:
        return {"error": "Usuario no encontrado"}
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/user/delete/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user is None:
        return {"error": "Usuario no encontrado"}
    db.delete(db_user)
    db.commit()
    return {"message": "Usuario eliminado con éxito"}

@router.get("/user/{user_id}" ,response_model=UserValidator)
def getUserbyId(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    return user

@router.get("/user/get/{name}" ,response_model=UserValidator)
def getUserbyName(name: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_name == name).first()
    return user

@router.get("/user/tipo/{tipo}" ,response_model=list[UserValidator])
def getUserbyTipo(tipo: int, db: Session = Depends(get_db)):
    users = db.query(User).filter(User.user_type == tipo).all()
    return users