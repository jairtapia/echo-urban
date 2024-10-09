from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.routers.drivers.model.Mdriver import DriverValidator
from app.routers.drivers.schema.Sdriver import Driver

router = APIRouter()

#solo para quitar algo
@router.get("/driver/all",response_model=list[DriverValidator])
def read_drivers(db: Session = Depends(get_db)):
    users = db.query(Driver).all()
    return users

@router.post("/driver/create", response_model=DriverValidator)
def create_driver(user: DriverValidator, db: Session = Depends(get_db)):
    db_driver = Driver(**user.dict())
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver

@router.put("/driver/edit/{driver_id}", response_model=DriverValidator)
def edit_driver(driver_id:int, driver: DriverValidator, db:Session = Depends(get_db)):
    db_driver = db.query(Driver).filter(Driver.driver_id == driver_id).first()
    if db_driver is None:
        return {"error": "Usuario no encontrado"}
    for key, value in driver.dict().items():
        setattr(db_driver, key, value)
    db.commit()
    db.refresh(db_driver)
    return db_driver

@router.delete("/driver/delete/{driver_id}", response_model=dict)
def delete_driver(driver_id: int, db: Session = Depends(get_db)):
    db_driver = db.query(Driver).filter(Driver.driver_id == driver_id).first()
    if db_driver is None:
        return {"error": "Usuario no encontrado"}
    db.delete(db_driver)
    db.commit()
    return {"message": "Usuario eliminado con éxito"}

@router.get("/driver/{driver_id}" ,response_model=DriverValidator)
def getDriverrbyId(driver_id: int, db: Session = Depends(get_db)):
    driver_db = db.query(Driver).filter(Driver.driver_id == driver_id).first()
    return driver_db