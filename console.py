#!/usr/bin/python3
"""
This module contains the command interpreter for the Airbnb project.
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the Airbnb project.
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Place",
                     "State", "City", "Amenity", "Review"]

    def do_quit(self, arg):
        """
            This Method  will exist the program
        """
        return True

    def do_EOF(self, arg):
        """
            This Method also Exits the program.
        """
        return True

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
        Method to print all instances of a given class or all instances.
        """
        args = arg.split()
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) > 1 and args[1] != "all()":
            print("** invalid command **")
        else:
            if len(args) == 1:
                print([str(obj) for obj in objects.values()
                       if type(obj).__name__ == args[0]])
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
            return

        cls_name = args[0]
        if cls_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        obj_key = "{}.{}".format(cls_name, obj_id)

        if obj_key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attr_value = args[3]
        obj = storage.all()[obj_key]

        try:
            attr_value = type(getattr(obj, attr_name))(attr_value)
        except Exception:
            pass

        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
