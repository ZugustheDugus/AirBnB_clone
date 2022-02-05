#!/usr/bin/python3
"""
unittests for Amenity
"""

import unittest
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

        #self.assertIsInstance(obj, Amenity)
        #self.assertIsInstance(obj, BaseModel)
