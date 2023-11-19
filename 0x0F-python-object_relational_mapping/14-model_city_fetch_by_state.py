#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (username, password, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).filter(
        State.id == City.state_id).order_by(State.id).all()

    for row in results:
        print('{}: ({}) {}'.format(row.State.name, row.City.id, row.City.name))
