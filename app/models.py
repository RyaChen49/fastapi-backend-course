from .database import Base
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
#Define Model
class Todo(Base):
        __tablename__="todos"
        id=Column(Integer,primary_key=True)
        title=Column(String(100),nullable=False)
        description=Column(String,nullable=False)
        completed=Column(Boolean,default=False)
        due_date = Column(Date, nullable=True)

class Users(Base):
        __tablename__="Users"
        id=Column(Integer, primary_key=True, index=True)
        username=Column(String,nullable=False)
        password=Column(String,nullable=False)
        email = Column(String, unique=True, nullable=False)