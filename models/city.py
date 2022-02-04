#!/usr/bin/python3
"""
This class stores info about cities.
City inherits from Base Model
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Init the class
    state_id: string - empty string: will be the State.id
    name: string - empty string
    """
    state_id = ""
    name = ""
