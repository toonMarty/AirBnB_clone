#!/usr/bin/python3
"""
This module contains a class that defines the console
"""
import cmd
# import argparse


class HBNBCommand(cmd.Cmd):
    """A class that defines the console
    """
    def __init__(self):
        """
        Initialize objects
        """
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command that exits the program"""
        return True

    def emptyline(self):
        """
        Method that adds an empty line after pressing enter key
        """
        pass

    # updated for Requirement 7. May be, branch. We'll branch
    '''def do_create(self, line):
        """Creates a new instance of BaseModel, saves it to the JSON
        file and prints the id
        Usage: create <arg>
        """
        if line is None:
            print('** class name missing **')

        if line != __class__.__name__:
            print("** class doesn't exist **")
        else:
            parser = argparse.ArgumentParser()
            args_str = __class__.__name__
            parser.parse_args(args_str.split())
    '''


if __name__ == "__main__":
    HBNBCommand().cmdloop()
