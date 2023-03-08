#!/usr/bin/python3
"""
    This module contains the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
        This class defines the command interpreter
    """
    prompt = "(hbnh) " #custom prompt
    
    def do_quit(self, arg):
        """
            This will exist the program
        """
        return True
    
    def do_EOF(self, arg):
        """
            This also Exits the program.
        """
        return True
    
    def emptyline(self):
        """
            Do nothing whem when emptyline + Enter
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
