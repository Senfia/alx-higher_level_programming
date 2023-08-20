#!/usr/bin/python3
"""
this script changes the name of a State object from the database
hbtn_0e_6_usa using SQLAlchemy
"""


import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: username password database_name")
    else:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                               (sys.argv[1], sys.argv[2], sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        state = session.query(State).filter_by(id=2).first()
        state.name = 'New Mexico'
        session.commit()
        session.close()
        engine.dispose()
