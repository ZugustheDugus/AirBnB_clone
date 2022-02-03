#!/usr/bin/python3
"""
This is the console that the user inputs commands into
"""


import cmd, sys, os, datetime, uuid, json

class HBNBCommand(cmd.Cmd):
    """Console class basic init"""
    intro = "Welcome to AirBnB!"
    prompt = "Select something"
    file = None

    def save(self, arg):
        """Save function"""
        self.file = open(arg, 'w')

    def close(self):
        """Close the Console"""
        if self.file:
            self.file.close()
            self.file = None

def parse(arg):
    """Convert args into tuples for interpretation"""
    return tuple(map(int,arg.split()))

if __name__ == '__main__':
    HBNBCommand().cmdloop()

