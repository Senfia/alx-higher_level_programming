#!/usr/bin/python3
"""
this script lists all State objects from the database hbtn_0e_6_usa
"""


import sys
import sqlalchemy
from model_state import Base, State

if __name__ == "__main__":
    engine = sqlalchemy.create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                                      .format(sys.argv[1],
                                              sys.argv[2], sys.argv[3]))
    query = "SELECT * FROM states"
    result = engine.execute(query)
    for row in result:
        tmp = str(row[0]) + ":" + " " + row[1]
        print(tmp)
