from sqlalchemy import Column, Integer, String, CheckConstraint
from database import Base

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer,CheckConstraint('id > 0',name='id_gt_zero'), primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

 