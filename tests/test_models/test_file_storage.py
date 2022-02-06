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
        #__objects = storage.all()
        #self.assertIsInstance(__objects, dict)
        #key = "{}.{}".format(obj.__class__.__name__, obj.id)
        #self.assertIn(key, __objects)
        #self.assertEqual(obj, __objects[key])
        #self.assertIsInstance(__objects[key], BaseModel)

    def test_save(self):
        """ Tests save method """
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
