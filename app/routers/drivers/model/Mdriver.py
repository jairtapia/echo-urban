from pydantic import BaseModel

class DriverValidator(BaseModel):
    driver_code: str
    user_id: int  # Este campo es opcional si no necesitas incluirlo
    driver_status: str
    work_hours: str

    class Config:
        orm_mode = True