import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id       = Column(Integer, primary_key = True)
    username = Column(String(250), nullable = False)
    password = Column(String(250), nullable = False)
    email    = Column(String(250), nullable = False)
    
