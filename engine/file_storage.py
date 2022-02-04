#!/usr/bin/python3
"""
File storage section of the program
"""

import json

from engine import file_storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """ 
    Serializes instance to JSON file and deserializes
    JSON files to instance
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """
        Returns the __objects
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        Adds new object to __objects
        """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                            obj.id)] = obj
        
    def save(self):
        """
        Serilizes __objects to json file at __file_path
        """
        obj_dict = {
            key: value.to_dict()
            for key, value in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(obj_dict, json_file)
