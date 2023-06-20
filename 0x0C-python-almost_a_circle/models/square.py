#!/usr/bin/python3
"""
Class Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class Constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Rectangle"""
        return "[Square] (" + str(self.id) + ") " + str(self.x) \
            + "/" + str(self.y) + " - " + str(self.size)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *x, **z):
        """Update variable"""
        j = ['id', 'size', 'x', 'y']
        i = 0
        if z:
            for key, value in z.items():
                setattr(self, key, value)
                i += 1
        if x:
            for c in x:
                setattr(self, j[i], c)
                i += 1


    def to_dictionary(self):
        """Square dict"""
        return ({"id": self.id, "size": self.size,
                "x": self.x, "y": self.y})
