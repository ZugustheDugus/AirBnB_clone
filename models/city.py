#!/usr/bin/python3
"""
This class stores info about cities.
City inherits from Base Model
"""

class City(BaseModel):
    """
    Init the class
    state_id: string - empty string: will be the State.id
    name: string - empty string
    """
    state_id = ""
    name = ""
    def __init__(self, id):