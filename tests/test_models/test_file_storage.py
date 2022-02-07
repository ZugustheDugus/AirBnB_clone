#!/usr/bin/python3
"""
unittests for File Storage
"""


import unittest
from models import storage
from models.base_model import BaseModel
import os

class TestFileStorage(unittest.TestCase):
    """
    unitests for File Storage
    1 -
    2 - test save
    """

    #def test_all(self):

        #obj = BaseModel()
        #__args = storage.all()
        #self.assertIsInstance(__args, dict)
        #key = "{}.{}".format(type(obj).__name__, obj.id)
        #self.assertIn(key, __args)
        #self.assertEqual(obj, __args[key])
        #self.assertIsInstance(__args[key], BaseModel)

    def test_reload(self):
        """
        Tests reload method
        """

        from json import dumps

        # Check if reloading without doing anything reloads the same thing
        old_dict = storage.all()
        storage.reload()
        new_dict = storage.all()
        self.assertEqual(old_dict.keys(), new_dict.keys())

        # Make new object and a dictionary for that object
        obj = BaseModel()
        obj.id = 1
        dict_dict = {"BaseModel.1": obj.to_dict()}
        obje_dict = {"BaseModel.1": obj}

        # Overwrite file.json so that it includes just this dictionary
        if os.path.exists("file.json"):
            os.remove("file.json")
        with open("file.json", 'w') as f:
            f.write(dumps(dict_dict))

        # Reload
        storage.reload()
        self.assertEqual(storage.all().keys(), obje_dict.keys())

    def test_save(self):
        """
        Tests save method
        """
        # storage = FileStorage()
        file = "file.json"
        # Remove file if it exists
        if os.path.exists(file):
            os.remove(file)
        # Test if save creates the file
        storage.save()
        self.assertTrue(os.path.exists(file))
        # Overwrite created file
        with open(file, 'w') as f:
            f.write("Anything")
        # Check if save overwrites existing files
        with open(file, 'r') as f:
            info = f.read()
            storage.save()
            new_info = f.read()
        self.assertNotEqual(info, new_info)

def test_new(self):
        """
        Tests new method
        """
        # create storage instance and instance of BaseModel
        obj = BaseModel()
        # create dictionary to set obj values to with **kwargs
        new_dict = {}
        new_dict["id"] = "456789"
        new_dict["created_at"] = "2021-2-2T10:29:35.678910"
        new_dict["updated_at"] = "2011-1-4T7:26:05.456789"
        obj2 = BaseModel(**new_dict)
        key = "{}.{}".format(type(obj2).__name__, obj2.id)
        self.assertNotIn(key, storage.all())
        obj2 = BaseModel()
        key = "{}.{}".format(type(obj2).__name__, obj2.id)
        __objects = storage.all()
        self.assertIn(key, __objects)
        self.assertEqual(obj2, __objects[key])
