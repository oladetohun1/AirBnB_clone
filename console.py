#!/usr/bin/python3
"""
This module contains the command interpreter for the Airbnb project.
"""

import cmd
import re
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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
        if len(argl) > 0 and argl[0] not in self.valid_classes:
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

    def my_count(self, class_n):
        """
        Method to count the number of instances of a class.
        """
        count = 0
        for key, value in storage.all().items():
            if class_n in key:
                count += 1
        print(count)

    def default(self, line):
        """Method to take care of following commands:
        <class name>.all()
        <class name>.count()
        <class name>.show(<id>)
        <class name>.destroy(<id>)
        <class name>.update(<id>, <attribute name>, <attribute value>)
        <class name>.update(<id>, <dictionary representation)
        Description:
            Creates a list representations of functional models
            Then use the functional methods to implement user
            commands, by validating all the input commands
        """
        
        valid_commands = ["all", "count", "show", "destroy", "update"]

        # Parse the input line using regular expressions
        match = re.match(r"^(\w+)\.(\w+)\((.*)\)$", line)
        if not match:
            return super().default(line)

        class_name, command_name, args_str = match.groups()

        # Check if the class and command are valid
        if class_name not in self.valid_classes or command_name not in valid_commands:
            return super().default(line)

        # Call the appropriate method based on the command
        method = getattr(self, "do_" + command_name)
        if command_name == "all" or command_name == "count":
            method(class_name)
        elif command_name == "show" or command_name == "destroy":
            id = args_str.strip(")")
            method("{} {}".format(class_name, id))
        elif command_name == "update":
            # Check if the arguments are valid
            if "," not in args_str:
                return super().default(line)

            id, rest = args_str.split(",", maxsplit=1)
            if rest.startswith("{"):
                # Update with dictionary representation
                try:
                    update_dict = eval(rest)
                except:
                    return super().default(line)
                for k, v in update_dict.items():
                    method("{} {} {} {}".format(class_name, id, k, v))
            else:
                # Update with attribute name and value
                rest = rest.strip()
                if "," not in rest:
                    return super().default(line)
                attr_name, attr_value = rest.split(",", maxsplit=1)
                method("{} {} {} {}".format(class_name, id, attr_name, attr_value))



if __name__ == "__main__":
    HBNBCommand().cmdloop()
