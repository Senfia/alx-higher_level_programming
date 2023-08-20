#!/usr/bin/python3
"""
This is module relationship_state
defines the relationship of the state class
"""


from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sq

Base = declarative_base()


class State(Base):
    """
    Class State
    """
    __tablename__ = "states"
    id = sq.Column(sq.Integer, primary_key=True, nullable=False)
    name = sq.Column(sq.String(128), nullable=False)

    cities = sq.orm.relationship("City", backref="state",
                                 cascade="all, delete, delete-orphan")

    def __str__(self):
        """fancy printing"""
        return "{}: {}".format(self.id, self.name)

    def __repr__(self):
        """print a class"""
        return "State(name={}, id={})".format(self.name, self.id)
