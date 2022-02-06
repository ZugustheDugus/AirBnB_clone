#!/usr/bin/python3
"""
unittests for Review
"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReviewClass(unittest.TestCase):
    """
    unittests for Review
    """

    def test_class(self):
        """
        1 - tests for empty class in fields
        2 - testing if BaseModel is parent of Review
        """
        obj = Review()

        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
        self.assertEqual(obj.place_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.text, "")

        self.assertIsInstance(obj, Review)
        self.assertIsInstance(obj, BaseModel)

        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("place_id", Review.__dict__)
        self.assertIn("user_id", Review.__dict__)
        self.assertIn("text", Review.__dict__)
