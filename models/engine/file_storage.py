#!/usr/bin/python3
"""
File storage section of the program
Sentence
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    serializes and/or deserializes JSON file
    Private attrs:
    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary - will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """
        dict of save objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        stores obj in dict above
        """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        obj_dict = {
            key: value.to_dict()
            for key, value in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):

        """
        reload: deserializes the JSON file to __objects JSON file if
        the JSON file (__file_path) exists;
        otherwise, do nothing. No exception should be raised)
        """

        try:
            with open(FileStorage.__file_path, "r") as json_file:
                obj_dict = json.load(json_file)
                for obj_str in obj_dict.values():
                    cls = eval(obj_str["__class__"])
                    new_obj = cls(**obj_str)
                    self.new(new_obj)

        except FileNotFoundError:
            pass