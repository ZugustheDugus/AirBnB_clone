#!/usr/bin/python3
"""
unittests for Amenity
"""

import unittest
import models
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """
    unittests for Amenity
    1 - tests if emoty string used
    2 - tests if BaseClass is parent of Amenity
    """

    def test_class(self):
        obj = Amenity()

        self.assertEqual(Amenity.name, "")

        self.assertIsInstance(obj, Amenity)
        self.assertIsInstance(obj, BaseModel)

        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("name", Amenity.__dict__)
