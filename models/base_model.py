#!/usr/bin/python3
"""
This is the base class from which other classes are derived
"""
import sys, os, uuid, json, datetime, models

__nb_objects = 0

class BaseModel():


    @classmethod
    def clear(cls):
        """Clear variables for testing purposes"""
        BaseModel.__nb_objects = 0

    def __init__(self, *args, **kwargs):
        """init the class"""
        TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, TIME_FORMAT)
                elif key == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value
            else:
                models.storage.new(self)

    def __str__(self):
        """Return string representation of the class"""
        return ("{}, {}, {}".format(self.__class__.__name__, self.id,
                                    self.__dict__))

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

    def save(self):
        """Updates updated_at public instance variable"""
        self.updated_at = datetime.today()
        models.storage.save()
    
    @classmethod
    def to_dict(self):
        dict_repr = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dict_recpt[key] = value.isoformat()
            else:
                dict_repr["__class__"] = self.__class__.__name__

        dict_repr["__class__"] = self.__class__.__name__

        return dict_repr
    
