#!/usr/bin/python3
"""HBNB Console Implementation"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import re
from shlex import split


def parse(arg):
    """Parses arguments from line"""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class represents the console"""
    prompt = '(hbnb) '
    __classes = [
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review"
    ]

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }

        match = re.search(r"\.", arg)
        if match is not None:
            cmd_args = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", cmd_args[1])
            if match is not None:
                command = [cmd_args[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(cmd_args[0], command[1])
                    return arg_dict[command[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieves the number of instances of a class"""
        cmd_args = parse(arg)
        storage_objects = storage.all()
        count = 0
        for v in storage_objects.values():
            if v.__class__.__name__ == cmd_args[0]:
                count += 1
        print(count)

    def do_create(self, arg):
        """Usage: create <class>
        Create command to create a new instance"""
        cmd_args = parse(arg)
        if not arg:
            print("** class name missing **")
        elif arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(cmd_args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Usage: show <class> <id>
        Prints the string representation of an instance
        based on the class name and id"""
        cmd_args = parse(arg)
        if len(cmd_args) == 0:
            print("** class name missing **")
        elif cmd_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(cmd_args) == 1:
            print("** instance id missing **")
        elif f"{cmd_args[0]}.{cmd_args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{cmd_args[0]}.{cmd_args[1]}"])

    def do_destroy(self, arg):
        """usage: destroy <class> <id>
        Deletes an instance based on the class name and id"""
        cmd_args = parse(arg)
        if len(cmd_args) == 0:
            print("** class name missing **")
        elif cmd_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(cmd_args) == 1:
            print("** instance id missing **")
        elif f"{cmd_args[0]}.{cmd_args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[f"{cmd_args[0]}.{cmd_args[1]}"]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Prints all string representation of all
        instances based or not on the class name"""
        cmd_args = parse(arg)
        storage_objects = storage.all()
        to_print = []
        if len(cmd_args) == 0:
            for v in storage_objects.values():
                to_print.append(str(v))
        elif cmd_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for v in storage_objects.values():
                if v.__class__.__name__ == cmd_args[0]:
                    to_print.append(str(v))

        if len(to_print) > 0:
            print(to_print)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value>
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        cmd_args = parse(arg)
        storage_objects = storage.all()

        if len(cmd_args) == 0:
            print("** class name missing **")
            return False
        elif cmd_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        elif len(cmd_args) == 1:
            print("** instance id missing **")
            return False
        elif f"{cmd_args[0]}.{cmd_args[1]}" not in storage.all():
            print("** no instance found **")
            return False
        elif len(cmd_args) == 2:
            print("** attribute name missing **")
            return False
        elif len(cmd_args) == 3:
            try:
                type(eval(cmd_args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(cmd_args) == 4:
            setattr(storage_objects[f"{cmd_args[0]}.{cmd_args[1]}"],
                    cmd_args[2], cmd_args[3])
        elif type(eval(cmd_args[2])) == dict:
            for k, v in eval(cmd_args[2]).items():
                setattr(storage_objects[f"{cmd_args[0]}.{cmd_args[1]}"],
                        k, v)
        else:
            setattr(storage_objects[f"{cmd_args[0]}.{cmd_args[1]}"],
                    cmd_args[2], cmd_args[3])
        storage_objects[f"{cmd_args[0]}.{cmd_args[1]}"].save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
