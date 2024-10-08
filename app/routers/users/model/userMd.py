from pydantic import BaseModel
from datetime import date
from typing import Optional

class UserValidator(BaseModel):
    user_name: str
    last_name_f: str
    last_name_m: str
    registration_date: date
    user_type: int
    class Config:
        orm_mode = True

