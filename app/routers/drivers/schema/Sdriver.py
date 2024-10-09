from sqlalchemy import Column, SmallInteger, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Driver(Base):
    __tablename__ = 'Driver'
    driver_id = Column(SmallInteger, primary_key=True ,index=True)
    driver_code = Column(String(10), nullable=False)
    user_id = Column(SmallInteger,ForeignKey("User.user_id"),nullable=False)
    driver_status = Column(String(10),nullable=False)
    work_hours = Column(String(20),nullable=False)
    