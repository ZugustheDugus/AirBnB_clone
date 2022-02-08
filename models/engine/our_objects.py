#!/usr/bin/python3
"""
Classes
"""

from ..base_model import BaseModel
from ..amenity import Amenity
from ..city import City
from ..place import Place
from ..review import Review
from ..state import State
from ..user import User

classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User,
    }

class_funcs = ["all", "count", "show", "destroy", "update"]
