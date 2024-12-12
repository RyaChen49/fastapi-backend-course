from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#Database
DATABASE_URL="sqlite:///./todos.db"
Base=declarative_base()
engine=create_engine(DATABASE_URL,connect_args={"check_same_thread":False})
Sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)