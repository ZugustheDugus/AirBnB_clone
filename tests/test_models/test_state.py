#!/usr/bin/python3
"""
unittests for State
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestStateClass(unittest.TestCase):
    """
    unittests for State
    """

    def test_class(self):
        """
        1 - tests if empty string passed
        2 - tests of BaseModel is parent of State
        """
        obj = State()

        self.assertEqual(State.name, "")
        self.assertEqual(obj.name, "")

        self.assertIsInstance(obj, State)
        self.assertIsInstance(obj, BaseModel)

        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("name", State.__dict__)
