#!/usr/bin/python3
"""
File storage section of the program
Sentence
"""

from os.path import exists
from json import loads, dumps


class FileStorage():
    """
    serializes and/or deserializes JSON file
    Private attrs:
    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary - will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        dict of save objects
        """
        return self.__objects

    def new(self, obj):
        """
        stores obj in dict above
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj
        self.save()

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        dict_store = {}
        for key, value in self.__objects.items():
            dict_store[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            f.write(dumps(dict_store))

    def reload(self):
        """
        reload: deserializes the JSON file to __objects JSON file if
        the JSON file (__file_path) exists;
        otherwise, do nothing. No exception should be raised)
        """
        if exists(self.__file_path) is False:
            return

        with open(self.__file_path, 'r') as f:
            dicts = loads(f.read())

        from .our_objects import classes

        self.__objects = {}
        for id in dict in dicts.items():
            class_name = id.split(".")[0]
            cls = classes[class_name]
            self.__objects[id] = cls(**dict)
