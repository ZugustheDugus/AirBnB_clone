#!/usr/bin/python3
"""
unittests for BaseModel
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    unittests for BaseModel
    1 - checks if correct types are used for attrs
    """

    def test_base(self):
        obj = BaseModel()

        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(BaseModel.id, "")
        self.assertEqual(BaseModel.to_dict, "")
        self.assertEqual(BaseModel.__nb_objects, "")
        self.assertEqual(BaseModel.__class__, "")
        self.assertEqual(BaseModel.__init__, "")
