#!/usr/bin/python3
"""
This is module relationship_city
defines the relationship of the city class
"""


from relationship_state import Base
import sqlalchemy as sq


class City(Base):
    """
    Class City
    """
    __tablename__ = "cities"
    id = sq.Column(sq.Integer, primary_key=True, nullable=False)
    name = sq.Column(sq.String(128), nullable=False)
    state_id = sq.Column(sq.Integer, sq.ForeignKey('states.id'),
                         nullable=False)

    def __str__(self):
        """printing"""
        return "{}: {}".format(self.id, self.name)

    def __repr__(self):
        """print the class"""
        return "City(name={}, id={}, state_id={})".format(
            self.name, self.id, self.state_id)
