
from sqlalchemy import Column, SmallInteger, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class UserType(Base):
    __tablename__ = 'UserType'
    user_type_id = Column(SmallInteger, primary_key=True, index=True)
    user_type_name = Column(String(50), nullable=False)
class User(Base):
    __tablename__ = 'User'
    user_id = Column(SmallInteger, primary_key=True, index=True)
    user_name = Column(String(50), nullable=False)
    last_name_f = Column(String(50), nullable=True)
    last_name_m = Column(String(50), nullable=True)
    registration_date = Column(Date, nullable=False)  # O el tipo que necesites
    user_type = Column(SmallInteger, ForeignKey("UserType.user_type_id"), nullable=False)

