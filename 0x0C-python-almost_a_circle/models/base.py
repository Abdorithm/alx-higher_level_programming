#!/usr/bin/python3
"""Defines the base class"""
import json
import csv


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
        """writes the JSON string representation
        of list_objs to a file:"""
        toBeSaved = []
        if list_objs is not None:
            for obj in list_objs:
                toBeSaved.append(obj.to_dictionary())
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(toBeSaved))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the
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
        """deserializes in JSON"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                wasSaved = Base.from_json_string(f.read())
            return [cls.create(**each) for each in wasSaved]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in csv"""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'w', encoding="utf-8") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    csvFormat = ['id', 'width', 'height', 'x', 'y']
                else:
                    csvFormat = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, csvFormat)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in csv"""
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                if cls.__name__ == "Rectangle":
                    csvFormat = ["id", "width", "height", "x", "y"]
                else:
                    csvFormat = ["id", "size", "x", "y"]
                reader = csv.DictReader(f, csvFormat)
                loadedList = []
                for row in reader:
                    tmpDict = {}
                    for key, value in row.items():
                        tmpDict[key] = int(value)
                    loadedList.append(tmpDict)
            return [cls.create(**each) for each in loadedList]
        except IOError:
            return []
