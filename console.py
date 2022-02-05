#!/usr/bin/python3
"""
This is the console that the user inputs commands into
"""


import cmd

from models.engine.file_storage import file_storage
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
    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        and saves to a JSON file, then prints
        """
        arg_list = HBNBCommand.parse(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif len(arg_list) > 1:
            print("** too many arguments **")
        elif (arg_list[0] in HBNBCommand.__class_list.keys()):
            new_obj = HBNBCommand.__class_list[arg_list[0]]()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    @classmethod
    def do_destroy(self, arg):
        """
        Deletes an instance based on class name and ID
        """
        arg_list = HBNBCommand.parse(arg)
        file_storage.reload()
        db = file_storage.all()
        if not len(arg_list):
            print("** class name missing **")
        elif (arg_list[0] not in HBNBCommand.__class_list.keys()):
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]):
            print("** no instance found **")
        else:
            del db["{}.{}".format(arg_list[0], arg_list[1])]
            file_storage.save()

    def show(self, cls):
        """
        Gives all elements inside File Storage
        that are of instances of cls
        """
        pass

    def destroy(self, cls):
        """
        Gives all elements inside File Storage
        that are of instances of cls
        """
        pass

    def update(self, cls):
        """
        Gives all elements inside File Storage
        that are of instances of cls
        """
        pass

    @classmethod
    def default(self, line):
        """
        Handles what to do if there is no do method passed
        """
        line_p = HBNBCommand.parse(line, '.')
        if line_p[0] in HBNBCommand.__class_list.keys() and len(line_p) > 1:
            if line_p[1][:-2] in HBNBCommand.__class_funcs:
                func = line_p[1][:-2]
                cls = HBNBCommand.__class_list[line_p[0]]
                eval("self.do_" + func)(cls.__name__)
            else:
                super().default(line)
            return False

    @classmethod
    def all(self):

    @classmethod
    def update(self, cls):
        pass

    @classmethod
    def empty_line(self):
        """
        Does nothing. It's an empty line
        Overrides emptyline function
        """
        pass

    @classmethod
    def save(self, arg):
        """Save function"""
        self.file = open(arg, 'w')
    
    @classmethod
    def count(self, arg):
        """
        print number of elements in filestorage
        that are instances of cls
        """
        arg_list = HBNBCommand.parse(arg)
        if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.__class_list:
            print("** class doesn't exist **")
        else:
            obj1 = []
            for obj in file_storage.all().values():
                if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                    obj1.append(obj.__str__())
                elif len(arg_list) == 0:
                    obj1.append(obj.__str__())

    @staticmethod
    def parse(arg, id=''):
        """Parser for the console"""

    @classmethod
    def help_create(self):
        """Help message for the create command"""
        print("""Creates a new instance of the first argument
                stores it in JSON file and prints its ID""")

    @classmethod
    def do_show(self, arg):
        """
        Prints string representation of an instance
        based on class name and id
        """
        arg_list = HBNBCommand.parse(arg)
        db = file_storage.all()
        if not len(arg_list):
            print("** class name missing **")
        elif (arg_list[0] not in HBNBCommand.__class_list.keys()):
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id is missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in db:
            print("** no instance **")
        else:
            print(db["{}.{}".format(arg_list[0], arg_list[1])])

    @classmethod
    def do_quit(self):
        """Quits the program"""
        return True

    @classmethod
    def help_quit(self):
        """Prints help message about quit command"""
        print("Quit command to exit the program\n")

    @classmethod
    def do_EOF(self):
        """End of file"""
        print("")
        return True


    @classmethod
    def close(self):
        """Close the Console"""
        if self.file:
            self.file.close()
            self.file = None

if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()