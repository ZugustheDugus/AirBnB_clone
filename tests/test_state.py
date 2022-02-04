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
        """
        obj = State()
        self.assertEqual(State.name, "")
        self.assertEqual(obj.name, "")
