#!/usr/bin/python3
"""
User class stores user info
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    init the class
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
