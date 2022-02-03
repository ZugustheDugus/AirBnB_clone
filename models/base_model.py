#!/usr/bin/python3
"""
This is the base class from which other classes are derived
"""
import sys
import os
import uuid
import json


class BaseModel():
    """init the class"""
    def __init__(self, id):
        super().__init__(id)
    
    def created_at(self):
        """Assign date time on creation"""
    
    def updated_at(self):
        """Assign date time on update"""

    def save(self):
        """Saves attributes"""
        save = save.self
    
    def __str__(self):
        """__str__ string"""