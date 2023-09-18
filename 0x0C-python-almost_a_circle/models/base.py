#!/usr/bin/python3
"""Defines the base class"""
import json
import os.path


class Base():
    """Represents Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes base class
            Args:
                id (int):
            Returns:
                None"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation
        of list_objs to a file:"""
        toBeSaved = []
        if list_objs is not None:
            for obj in list_objs:
                toBeSaved.append(obj.__dict__)
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(toBeSaved))

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the
        JSON string representation json_string:"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            rec = cls(2, 4)
            rec.update(**dictionary)
            return rec
        else:
            sq = cls(3)
            sq.update(**dictionary)
            return sq

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        list_objs = []
        if os.path.isfile(filename) is False:
            return list_objs
        with open(filename, 'r', encoding="utf-8") as f:
            wasSaved = json.load(f)
        for each in wasSaved:
            list_objs.append(cls.create(**each))
        return list_objs
