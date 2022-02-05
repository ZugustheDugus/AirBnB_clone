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
