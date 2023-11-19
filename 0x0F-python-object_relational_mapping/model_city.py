#!/usr/bin/python3
"""
The class definition of a City
"""
from sqlalchemy import create_engine, ForeignKey, \
        Column, String, Integer, VARCHAR
from model_state import Base, State
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class City(Base):
    """
    Create the Class City
    """
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', VARCHAR(128), nullable=False)
    state_id = Column('state_id', Integer,
                      ForeignKey('State.id'), nullable=False)
