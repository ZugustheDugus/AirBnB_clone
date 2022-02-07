#!/usr/bin/python3
"""
unittests for BaseModel
"""
import unittest
import os
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    unittests for BaseModel
    1 - checks if correct types are used for attrs
    2 - checks if attrs in dict are set correctly
    3 - checks to see if obj is instance of BaseModel
    """

    def test_base(self):
        obj = BaseModel()

        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)

        self.assertIsInstance(obj, BaseModel)

        new_nary = {}
        new_nary["id"] = "234567"
        new_nary["created_at"] = "2011-2-2T10:23:25.345678"
        new_nary["updated_at"] = "2021-1-4T7:35:05.123456"

        obj2 = BaseModel(**new_nary)
        self.assertIsInstance(obj2, BaseModel)
        self.assertIn("id", obj2.__dict__)
        self.assertIn("created_at", obj2.__dict__)
        self.assertIn("updated_at", obj2.__dict__)
        self.assertIsInstance(obj2.id, str)
        self.assertIsInstance(obj2.created_at, datetime)
        self.assertIsInstance(obj2.updated_at, datetime)
        self.assertEqual(obj2.id, "234567")
        string = "2011-02-02 10:23:25.345678"
        self.assertEqual("{}".format(obj2.created_at), string)
        string = "2021-01-04 07:35:05.123456"
        self.assertEqual("{}".format(obj2.updated_at), string)

    def test_str(self):
        """
        Tests __str__ method
        """
        obj = BaseModel()
        cls = type(obj).__name__
        string = "[{}] ({}) {}".format(cls, obj.id, obj.__dict__)
        self.assertEqual(obj.__str__(), string)

    def test_save(self):
        """
        Tests save method
        """
        obj = BaseModel()
        x = obj.updated_at
        obj.save()
        y = obj.updated_at
        self.assertNotEqual(x, y)
