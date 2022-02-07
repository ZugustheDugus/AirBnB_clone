#!/usr/bin/python3
"""
This is the console that the user inputs commands into
"""


import cmd
from json import loads, dumps
from uuid import UUID, uuid1, uuid3, uuid4
import uuid
from models import storage

from models.engine import file_storage
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
    intro = "Welcome to AirBnB!"
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

    def help_quit(self, arg):
        """Prints help message about quit command"""
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """End of file"""
        print("")
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        and saves to a JSON file, then prints
        """
        arg_list = HBNBCommand.parse(arg)
        new_obj = ''
        storage.reload()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif len(arg_list) > 1:
            print("** too many arguments **")
        elif (arg_list[0] in HBNBCommand.classes.keys()):
            new_obj = HBNBCommand.classes[arg_list[0]]
            new_obj.id = uuid4()
            print("{}".format(new_obj.id))
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """Help message for the create command"""
        print("""Creates a new instance of the first argument
                stores it in JSON file and prints its ID""")

    def do_show(self, arg):
        """
        Prints string representation of an instance
        based on class name and id
        """
        arg_list = HBNBCommand.parse(arg)
        db = storage.all()
        if not len(arg_list):
            print("** class name missing **")
        elif (arg_list[0] not in HBNBCommand.classes.keys()):
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id is missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in db:
            print("** no instance found**")
        else:
            print(db["{}.{}".format(arg_list[0], arg_list[1])])
    
    def help_show(self):
        """Prints the help message for do_show command"""
        print("""Prints the string representation of an instance
                based on class name and id""")

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name and ID
        """
        arg_list = HBNBCommand.parse(arg)
        storage.reload()
        db = storage.all()
        if not len(arg_list):
            print("** class name missing **")
        elif (arg_list[0] not in HBNBCommand.classes.keys()):
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]):
            print("** no instance found **")
        else:
            del db["{}.{}".format(arg_list[0], arg_list[1])]
            storage.save()
    
    def help_destroy(self):
        """Prints the help message for the do_destroy command"""
        print("""Deletes an instance based on class name and id""")

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
                whether based on class or not""")

    def do_update(self, arg):
        """
        Updates an instance based on class name and id
        by adding or updating an attribute and saving the change
        into a JSON file
        """
        arg_list = HBNBCommand.parse(arg)
        obj_dict = storage.all()

        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if (arg_list[0] not in HBNBCommand.classes.keys()):
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        string = arg[0] + "." + arg[1]
        if string not in obj_dict.keys():
            print("** no instance found **")
            return False
        if "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            print("** value missing **")
            return False
        try:
            a = float(arg[3])
            if a.is_integer():
                a = int(a)
        except (TypeError, ValueError):
            setattr(obj_dict[string], arg[2], str(arg[3]))
            storage.save()
            return False
        setattr(obj_dict[string], arg[2], a)
        storage.save()

    def help_update(self):
        """
        Prints the help message for the do_update command
        """
        print("""Updates an instance based on class name and id
        by adding or updating an attribute and saving the change
        into a JSON file""")

    def empty_line(self):
        """
        Does nothing. It's an empty line
        Overrides emptyline function
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

    def default(self, line):
        """
        Handles what to do if there is no valid do method passed
        """
        line_p = HBNBCommand.parse(line, '.')
        if line_p[0] in HBNBCommand.classes.keys() and len(line_p) > 1:
            if line_p[1][:-2] in HBNBCommand.class_funcs():
                func = line_p[1][:-2]
                cls = HBNBCommand.classes[line_p[0]]
                eval("self.do_" + func)(cls.__name__)
            else:
                super().default(line)
            return False

    def save(self, arg):
        """Save function"""
        self.file = open(arg, 'w')

    def close(self):
        """Close the Console"""
        if self.file:
            self.file.close()
            self.file = None

if __name__ == '__main__':
    HBNBCommand().cmdloop()