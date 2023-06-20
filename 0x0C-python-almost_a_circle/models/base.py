#!/usr/bin/python3
"""
Base class Module
"""

import json
import csv


class Base():
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """create an object from json file"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects


    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        static method that returns the json string
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        
        """
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """
        create class method
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy = cls(1, 1)
        elif cls is Square:
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads from file"""
        from os import path
        filename = cls.__name__ + ".json"
        if not path.isfile(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves object to csv."""
        filename = cls.__name__ + ".csv"
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)


    @classmethod
    def load_from_file_csv(cls):
        """Loads object to csv."""
        filename = cls.__name__ + ".csv"
        from models.rectangle import Rectangle
        from models.square import Square
        new = []
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                new.append(cls.create(**d))
        return new

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares"""
        import turtle
        from random import randint

        lists = list_rectangles + list_squares
        turtle.colormode(255)
        turtle.bgcolor("blue")
        t = turtle.Turtle()
        t.shape("turtle")
        t.color("#ffffff")
        j = -200
        y = -255
        i = 0
        length = len(lists)

        while i < length:
            current_item = lists[i]
            t.pensize(0)
            t.color((randint(1, 255), randint(1, 255), randint(1, 255)))
            t.goto(j, y)
            j += 70
            y += 60
            t.pensize(10)
            for r in range(2):
                t.back(current_item.width)
                t.right(90)
                t.back(current_item.height)
                t.right(90)
            t.left(50)
            i += 1

        turtle.exitonclick()
