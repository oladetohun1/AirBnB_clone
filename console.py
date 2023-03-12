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

valid_classes = ["BaseModel", "User", "Place",
                 "State", "City", "Amenity", "Review"]


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
            This Method Exits the program.
        """
        return True

    def emptyline(self):
        """
        Method to handle an empty line.
        """
        pass

    def do_create(self, arg):
        """This method creates a new instance of BaseModel
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
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        argl = arg.split()
        if len(argl) > 0 and argl[0] not in valid_classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, arg):
        """
        Method to update an instance attribute.
        Update an instance based on the class name and id with a dictionary:
        <class name>.update(<id>, <dictionary representation>)
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        elif args[1] not in self.ids[args[0]]:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** dictionary missing **")
            return
        try:
            obj_dict = eval('{' + ' '.join(args[2:]) + '}')
        except:
            print("** invalid syntax for dictionary **")
            return
        obj = self.classes[args[0]].objects[args[1]]
        obj.__dict__.update(obj_dict)
        storage.save()


    def my_count(self, class_n):
        """
        Method to count the number of instances of a class.
        """
        count = 0
        for key, value in storage.all().items():
            if class_n in key:
                count += 1
        print(count)

    def default(self, arg):
        """
        Method to handle the default case.
        """
        args = arg.split(".")
        if len(args) > 1:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                self.my_count(args[0])
            elif args[1].startswith("show("):
                id = args[1].split("(")[1].split(")")[0]
                self.do_show("{} {}".format(args[0], id))
            elif args[1].startswith("destroy("):
                id = args[1].split("(")[1].split(")")[0]
                self.do_destroy("{} {}".format(args[0], id))
            elif args[1].startswith("update("):
                id = args[1].split("(")[1].split(",")[0]
                attr = args[1].split(",")[1].split(")")[0]
                value = args[1].split(",")[2].split(")")[0]
                self.do_update("{} {} {} {}".format(args[0], id, attr, value))
            else:
                print("*** Unknown syntax: {}".format(arg))
        else:
            print("*** Unknown syntax: {}".format(arg))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
