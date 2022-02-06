#!/usr/bin/python3
"""
Unittests for City
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCityClass(unittest.TestCase):
    """
    unittests for City
    1 - tests if empty string passed
    """

    def test_class(self):

        obj = City()

        self.assertEqual(City.name, "")
        self.assertEqual(City.state_id, "")
        self.assertEqual(obj.name, "")
        self.assertEqual(obj.state_id, "")

        self.assertIsInstance(obj, City)
        self.assertIsInstance(obj, BaseModel)

        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("name", City.__dict__)
        self.assertIn("state_id", City.__dict__)
