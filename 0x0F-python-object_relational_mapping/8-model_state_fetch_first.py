#!/usr/bin/python3
"""
this script prints all states from the database
hbtn_0e_6_usa using SQLAlchemy
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), echo=False)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    result = session.query(State.id, State.name).order_by(State.id).first()
    if result:
        print("{:d}: {}".format(result[0], result[1]))
    else:
        print("Nothing")

    session.close()
    engine.dispose()
