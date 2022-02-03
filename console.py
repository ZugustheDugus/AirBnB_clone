#!/usr/bin/python3
"""
This is the console that the user inputs commands into
"""


import cmd

from engine import file_storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Console class basic init"""
    intro = "Welcome to AirBnB!"
    prompt = "(hbnb)"
    file = None
    
    __class_list = {
        BaseModel.__name__: BaseModel,
        User.__name__: User,
        State.__name__: State,
        City.__name__: City,
        Place.__name__: Place,
        Amenity.__name__: Amenity,
        Review.__name__: Review
    }
    __class_funcs = ["all", "count", "show", "destroy", "update"]


    @staticmethod
    def parse(arg):
        """Convert args into tuples for interpretation"""
        arg_list = arg.split(id)
        narg_list = []

        for a in arg_list:
            if a != '':
                narg_list.append(a)
        return narg_list

    @classmethod
    def create(self):

    @classmethod
    def show(self):

    @classmethod
    def destroy(self):

    @classmethod
    def default(self):

    @classmethod
    def all(self):

    @classmethod
    def update(self, cls):

    @classmethod
    def empty_line(self):
        """Does nothing. It's an empty line"""
        pass

    @classmethod
    def save(self, arg):
        """Save function"""
        self.file = open(arg, 'w')

    @classmethod
    def EOF(self):

    @classmethod
    def close(self):
        """Close the Console"""
        if self.file:
            self.file.close()
            self.file = None

if __name__ == '__main__':
    HBNBCommand().cmdloop()