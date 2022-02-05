#!/usr/bin/python3
"""
Unit tests battery for the console
"""


import unittest
from AirBnB_clone.console import HBNBCommand

class TestConsole(unittest.TestCase):
    """"""
    def test_console(self):
        """"""
        obj = HBNBCommand()
        self.assertEqual(HBNBCommand, "")
        self.assertEqual(HBNBCommand.default, "")
        self.assertEqual(HBNBCommand.destroy, "")
        self.assertEqual(HBNBCommand.do_all, "")
        self.assertEqual(HBNBCommand.do_create, "")
        self.assertEqual(HBNBCommand.close "")
        self.assertEqual(HBNBCommand.cmdloop, "")
        self.assertEqual(HBNBCommand.count, "")
        self.assertEqual(HBNBCommand.do_EOF, "")

        self.assertIsInstance(obj, HBNBCommand)
        self.assertIsInstance(cls, HBNBCommand)