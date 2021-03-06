#!/usr/bin/python3
"""
unittests for User
"""

import unittest
from models import user
from models.base_model import BaseModel
from models.user import User


class TestUserClass(unittest.TestCase):
    """
    tests for User
    1 - tests for empty strings in fields
    2 - tests if BaeModel is parent of User
    """
    def test_class(self):
        obj = User()
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")

        self.assertIsInstance(obj, User)
        self.assertIsInstance(obj, BaseModel)

        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("email", User.__dict__)
        self.assertIn("password", User.__dict__)
        self.assertIn("first_name", User.__dict__)
        self.assertIn("last_name", User.__dict__)
