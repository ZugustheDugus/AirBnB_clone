#!/usr/bin/python3
"""
This is the base class from which other classes are derived
"""
import sys
import os
import uuid
import json
import datetime
import abs

__nb_objects = 0

class BaseModel():


    @classmethod
    def clear(cls):
        """Clear variables for testing purposes"""
        BaseModel.__nb_objects = 0



    def __init__(self, id):
        """init the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def id(self):
        """Generate an id for the class using UUID"""
        id = uuid.uuid1()
        return id

    @classmethod
    def created_at(self):
        """Assign date time on creation"""
    
    @classmethod
    def updated_at(self):
        """Assign date time on update"""

    @classmethod
    def save(self):
        """Saves attributes"""
        save = save.self
    
    @classmethod
    def to_dict(self):
        attrs = {'id': self.id}
        return attrs
    
    def __str__(self):
        """__str__ string"""
        return ("[Class Name], {}, {}".format(id, __dict__))