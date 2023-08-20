#!/usr/bin/python3
"""
this script prints all states from the database
hbtn_0e_6_usa using SQLAlchemy
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session1 = sessionmaker(bind=engine)
    session2 = session1()
    instance = session2.query(State).first()
    if instance:
        print("{}: {}".format(instance.id, instance.name))
    else:
        print("Nothing")
