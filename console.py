#!/usr/bin/python3
"""
This module contains the command interpreter for the Airbnb project.
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the Airbnb project.
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

    def emptyline(self):
        """
        Method to handle an empty line.
        """
        pass

    def do_create(self, arg):
        """
        Method to create a new BaseModel instance.
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Method to print the string representation of an instance.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Method to delete an instance.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """
        Method to print all instances of a given class.
        """
        args = arg.split()
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in objects.values()
                   if type(obj).__name__ == args[0]])

    def do_update(self, arg):
        """
        Method to update an instance attribute.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj = storage.all()["{}.{}".format(args[0], args[1])]
            setattr(obj, args[2], type(getattr(obj, args[2]))(args[3]))
            obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

