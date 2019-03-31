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

# Create an engine that stores data in the local directory's
# sqlalchemy_messMatrix.db file.
engine = create_engine('sqlite3:///sqlalchemy_messMatrix.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
