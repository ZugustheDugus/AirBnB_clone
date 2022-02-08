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

        obj = BaseModel()
        obj.id = 1
        dict_dict = {"BaseModel.1": obj.to_dict()}
        obje_dict = {"BaseModel.1": obj}

        if os.path.exists("file.json"):
            os.remove("file.json")
        with open("file.json", 'w') as f:
            f.write(dumps(dict_dict))

        storage.reload()
        self.assertEqual(storage.all().keys(), obje_dict.keys())

    def test_save(self):
        """
        Tests save method
        """
        file = "file.json"
        if os.path.exists(file):
            os.remove(file)
        storage.save()
        self.assertTrue(os.path.exists(file))
        with open(file, 'w') as f:
            f.write("Anything")
        with open(file, 'r') as f:
            info = f.read()
            storage.save()
            new_info = f.read()
        self.assertNotEqual(info, new_info)

    def test_new(self):
        """
        Tests new method
        """
        obj = BaseModel()
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
