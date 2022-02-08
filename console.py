#!/usr/bin/python3
"""
This is the console that the user inputs commands into
"""


import cmd
from json import loads, dumps
from models import storage

from models.engine import file_storage, our_objects
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """Console class basic init"""
    #intro = "Welcome to AirBnB!"
    prompt = "(hbnb) "

    classes = {
        BaseModel.__name__: BaseModel,
        User.__name__: User,
        State.__name__: State,
        City.__name__: City,
        Place.__name__: Place,
        Amenity.__name__: Amenity,
        Review.__name__: Review
    }
    class_funcs = ["all", "count", "create", "show", "destroy", "update"]

    @staticmethod
    def parse(arg, id=" "):
        """Convert args into tuples for interpretation"""
        arg_list = arg.split(id)
        narg_list = []

        for a in arg_list:
            if a != '':
                narg_list.append(a)
        return narg_list

    def do_quit(self, arg):
        """Quits the program"""
        return True

    def do_EOF(self, arg):
        """EOF is same as do_quit and runs identically"""
        print()
        raise SystemExit

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        and saves to a JSON file, then prints
        """
        arg_list = HBNBCommand.parse(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif (arg_list[0] in HBNBCommand.classes.keys()):
            new_obj = HBNBCommand.classes[arg_list[0]]()
            new_obj.save()
            print("{}".format(new_obj.id))
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """Help message for the create command"""
        print("""Creates a new instance of the first argument
                stores it in JSON file and prints its ID\n""")

    def do_show(self, arg):
        """
        Prints string representation of an instance
        based on class name and id
        """
        arg_list = HBNBCommand.parse(arg)
        db = storage.all()
        arg = arg.split(" ")
        key = ".".join(arg)
        if not len(arg_list):
            print("** class name missing **")
        elif (arg_list[0] not in HBNBCommand.classes.keys()):
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id is missing **")
        else:
            try:
                print(db[key])
            except:
                print("** no instance found **")
    
    def help_show(self):
        """Prints the help message for do_show command"""
        print("""Prints the string representation of an instance
                based on class name and id\n""")

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name and ID
        """
        arg_list = HBNBCommand.parse(arg)
        arg = arg.split(" ")
        key = ".".join(arg)
        db = storage.all()
        if not len(arg_list):
            print("** class name missing **")
        elif (arg_list[0] not in HBNBCommand.classes.keys()):
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            try:
                del(db[key])
                storage.save()
            except:
                print("** no instance found **")
    
    def help_destroy(self):
        """Prints the help message for the do_destroy command"""
        print("""Deletes an instance based on class name and id\n""")

    def do_all(self, arg):
        """
        Prints string representation of all instances
        whether based on class or not
        """
        arg_list = HBNBCommand.parse(arg)
        if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj1 = []
            for obj in storage.all().values():
                if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                    obj1.append(obj.__str__())
                elif len(arg_list) == 0:
                    obj1.append(obj.__str__())
            print(obj1)

    def help_all(self):
        """Prints the help message for the do_all command"""
        print("""Prints string representation of all instances
                whether based on class or not\n""")

    def do_update(self, arg):
        """
        Updates an instance based on class name and id
        by adding or updating an attribute and saving the change
        into a JSON file
        """
        #arg_list = HBNBCommand.parse(arg)
        obj_dict = storage.all()
        arg = arg.split(" ")
        print(arg)
        if arg[0] == "":
            print("** class name missing **")
            return
        elif (arg[0] not in HBNBCommand.classes.keys()):
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        elif len(arg) == 2:
            print("** attribute name missing **")
            return
        elif len(arg) == 3:
            print("** value missing **")
            return
        key = arg[0] + "." + arg[1]
        if key not in obj_dict.keys():
            print("** no instance found **")
            return
        try:
            a = float(arg[3])
            if a.is_integer():
                a = int(a)
            setattr(obj_dict[key], arg[2], a)
        except (TypeError, ValueError):
            setattr(obj_dict[key], arg[2], (arg[3].strip("'")))
        storage.save()

    def help_update(self):
        """
        Prints the help message for the do_update command
        """
        print("""Updates an instance based on class name and id
        by adding or updating an attribute and saving the change
        into a JSON file\n""")

    def emptyline(self):
        """
        Does nothing. It's an empty line
        Overrides emptyline function\n
        """
        pass

    def do_count(self, arg):
        """
        print number of elements in filestorage
        that are instances of cls
        """
        arg_list = HBNBCommand.parse(arg)
        if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj1 = []
            for obj in storage.all().values():
                if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                    obj1.append(obj.__str__())
                elif len(arg_list) == 0:
                    obj1.append(obj.__str__())

if __name__ == '__main__':
    HBNBCommand().cmdloop()