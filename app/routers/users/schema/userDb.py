from sqlalchemy import Column, SmallInteger, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class UserSchema(Base):
    __tablename__ = 'railway.User'
    user_id = Column(SmallInteger, primary_key=True, index=True)
    user_name = Column(String(10), nullable=False)
    last_name_f = Column(String(15), nullable=False)
    last_name_m = Column(String(15), nullable=False)
    registration_date = Column(Date, nullable=False)
    user_type = Column(SmallInteger, ForeignKey('railway.Usertype.user_type_id'), nullable=False)
    usertype = relationship("UserType", back_populates="users")

class UserType(Base):
    __tablename__ = 'railway.Usertype'
    user_type_id = Column(SmallInteger, primary_key=True, index=True)
    type_name = Column(String(15), nullable=False)
    users = relationship("UserSchema", back_populates="Usertype")
