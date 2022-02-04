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
    """

    def test_class(self):
        self.assertEqual(Amenity.name, "")
