#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
"""Defines the HBnB console."""
=======
""" Defines entry point of the command interpreter."""
>>>>>>> c87e3fc5b29931544e403069576fd1a4865bb8de
import cmd
=======
"""This module defines the entry point of the command interpreter.

It defines one class, `HBNBCommand()`, which sub-classes the `cmd.Cmd` class.
This module defines abstractions that allows us to manipulate a powerful
storage system (FileStorage / DB). This abstraction will also allow us to
change the type of storage easily without updating all of our codebase.

It allows us to interactively and non-interactively:
    - create a data model
    - manage (create, update, destroy, etc) objects via a console / interpreter
    - store and persist objects to a file (JSON file)

Typical usage example:

    $ ./console
    (hbnb)

    (hbnb) help
    Documented commands (type help <topic>):
    ========================================
    EOF  create  help  quit

    (hbnb)
    (hbnb) quit
    $
"""
>>>>>>> a117c8d72be540ce70134bcadf324a2292836c3e
import re
=======
'''
Defines entry point of the command interpreter.
'''
>>>>>>> 5b613d50bb0fbaeaac59b32c00c4a33c1b3e813d
import cmd
import shlex
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
<<<<<<< HEAD
<<<<<<< HEAD
from models.state import State
from models.city import City
from models.place import Place
=======
from models.place import Place
from models.state import State
from models.city import City
<<<<<<< HEAD
>>>>>>> c87e3fc5b29931544e403069576fd1a4865bb8de
from models.amenity import Amenity
=======
from models.state import State
from models.city import City
>>>>>>> a117c8d72be540ce70134bcadf324a2292836c3e
from models.review import Review
from models.amenity import Amenity
from models.place import Place

<<<<<<< HEAD

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
<<<<<<< HEAD
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
=======
            return [index.strip(",") for index in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [index.strip(",") for index in lexer]
>>>>>>> c87e3fc5b29931544e403069576fd1a4865bb8de
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
<<<<<<< HEAD
        retl = [i.strip(",") for i in lexer]
=======
        retl = [index.strip(",") for index in lexer]
>>>>>>> c87e3fc5b29931544e403069576fd1a4865bb8de
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
<<<<<<< HEAD
    """Defines the HolbertonBnB command interpreter.
=======
    """
    Implements the class HBNBCommand.
>>>>>>> c87e3fc5b29931544e403069576fd1a4865bb8de
=======
current_classes = {'BaseModel': BaseModel, 'User': User,
                   'Amenity': Amenity, 'City': City, 'State': State,
                   'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """The command interpreter.

    This class represents the command interpreter, and the control center
    of this project. It defines function handlers for all commands inputted
    in the console and calls the appropriate storage engine APIs to manipulate
    application data / models.
>>>>>>> a117c8d72be540ce70134bcadf324a2292836c3e

    It sub-classes Python's `cmd.Cmd` class which provides a simple framework
    for writing line-oriented command interpreters.
    """
<<<<<<< HEAD
<<<<<<< HEAD

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
=======
    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"
            }

    def default(self, arg):
        """ Improves the default cmd. """
        argdict = {
                "show": self.do_show,
                "destroy": self.do_destroy,
                "all": self.do_all,
                "update": self.do_update,
                "count": self.do_count
                }
>>>>>>> c87e3fc5b29931544e403069576fd1a4865bb8de
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
<<<<<<< HEAD
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
=======

            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]

>>>>>>> c87e3fc5b29931544e403069576fd1a4865bb8de
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

<<<<<<< HEAD
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        argl = parse(arg)
=======
    def do_quit(self, args):
        """ Quit command to exit. """
        return True
=======

    prompt = "(hbnb) "

    def precmd(self, line):
        """Defines instructions to execute before <line> is interpreted.
        """
        if not line:
            return '\n'

        pattern = re.compile(r"(\w+)\.(\w+)\((.*)\)")
        match_list = pattern.findall(line)
        if not match_list:
            return super().precmd(line)

        match_tuple = match_list[0]
        if not match_tuple[2]:
            if match_tuple[1] == "count":
                instance_objs = storage.all()
                print(len([
                    v for _, v in instance_objs.items()
                    if type(v).__name__ == match_tuple[0]]))
                return "\n"
            return "{} {}".format(match_tuple[1], match_tuple[0])
=======
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''Implements the class HBNBCommand.'''
    prompt = '(hbnb) '
    __classes = [
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    ]

    def do_create(self, args):
        '''
        Creates a new instance of BaseModel, saves it
        '''
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0] + '()')
            models.storage.save()
            print(new_instance.id)

    def do_show(self, args):
        '''
        Printing the string representation
        '''
        strings = args.split()
        if len(strings) == 0:
            print("** class name missing **")
        elif strings[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(strings) == 1:
            print("** instance id missing **")
>>>>>>> 5b613d50bb0fbaeaac59b32c00c4a33c1b3e813d
        else:
            obj_dict = models.storage.all()
            key_value = strings[0] + '.' + strings[1]
            if key_value in obj_dict:
                print(obj_dict[key_value])
            else:
<<<<<<< HEAD
                match_json = re.findall(r"{.*}", match_tuple[2])
                if (match_json):
                    return "{} {} {} {}".format(
                        match_tuple[1], match_tuple[0],
                        re.sub("[\"\']", "", args[0]),
                        re.sub("\'", "\"", match_json[0]))
                return "{} {} {} {} {}".format(
                    match_tuple[1], match_tuple[0],
                    re.sub("[\"\']", "", args[0]),
                    re.sub("[\"\']", "", args[1]), args[2])

    def do_help(self, arg):
        """To get help on a command, type help <topic>.
        """
        return super().do_help(arg)
>>>>>>> a117c8d72be540ce70134bcadf324a2292836c3e

    def do_EOF(self, line):
        """Inbuilt EOF command to gracefully catch errors.
        """
        print("")
        return True
=======
                print("** no instance found **")

    def do_destroy(self, args):
        '''
        Deleting some instance
        '''
        args = args.split()
        objects = models.storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key_find = args[0] + '.' + args[1]
            if key_find in objects:
                objects.pop(key_find, None)
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, args):
        '''
        Printing a string representation of the whole instances
        '''
        args = args.split()
        objects = models.storage.all()
        new_list = []

        if len(args) == 0:
            for obj in objects.values():
                new_list.append(obj.__str__())
            print(new_list)
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in objects.values():
                if obj.__class__.__name__ == args[0]:
                    new_list.append(obj.__str__())
            print(new_list)

    def do_update(self, args):
        '''
        Update some instance
        '''
        objects = models.storage.all()
        args = args.split(" ")

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key_find = args[0] + '.' + args[1]
            obj = objects.get(key_find, None)
>>>>>>> 5b613d50bb0fbaeaac59b32c00c4a33c1b3e813d

            if not obj:
                print("** no instance found **")
                return

            setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
            models.storage.save()

    def check_class_name(self, name=""):
        """
<<<<<<< HEAD
        args = arg.split()
        if not validate_classname(args):
            return

<<<<<<< HEAD
>>>>>>> c87e3fc5b29931544e403069576fd1a4865bb8de
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
<<<<<<< HEAD
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        argl = parse(arg)
        objdict = storage.all()
=======
        """
        Prints the string representation of an instance.
        """
        argl = parse(arg)
        objd = storage.all()

>>>>>>> c87e3fc5b29931544e403069576fd1a4865bb8de
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
<<<<<<< HEAD
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        argl = parse(arg)
        objdict = storage.all()
=======
        elif "{}.{}".format(argl[0], argl[1]) not in objd:
=======
        new_obj = current_classes[args[0]]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance.
        """
        args = arg.split()
        if not validate_classname(args, check_id=True):
            return

        instance_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
>>>>>>> a117c8d72be540ce70134bcadf324a2292836c3e
            print("** no instance found **")
            return
        print(req_instance)

    def do_destroy(self, arg):
<<<<<<< HEAD
        """ Deletes an instance based on the class name and id."""
        argl = parse(arg)
        objd = storage.all()

>>>>>>> c87e3fc5b29931544e403069576fd1a4865bb8de
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
<<<<<<< HEAD
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        argl = parse(arg)
=======
        elif "{}.{}".format(argl[0], argl[1]) not in objd.keys():
=======
        """Deletes an instance based on the class name and id.
        """
        args = arg.split()
        if not validate_classname(args, check_id=True):
            return

        instance_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
>>>>>>> a117c8d72be540ce70134bcadf324a2292836c3e
            print("** no instance found **")
            return

        del instance_objs[key]
        storage.save()

    def do_all(self, arg):
        """Prints string representation of all instances.
        """
        args = arg.split()
        all_objs = storage.all()

<<<<<<< HEAD
>>>>>>> c87e3fc5b29931544e403069576fd1a4865bb8de
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
=======
        if len(args) < 1:
            print(["{}".format(str(v)) for _, v in all_objs.items()])
            return
        if args[0] not in current_classes.keys():
>>>>>>> a117c8d72be540ce70134bcadf324a2292836c3e
            print("** class doesn't exist **")
            return
        else:
<<<<<<< HEAD
            objl = []
<<<<<<< HEAD
=======

>>>>>>> c87e3fc5b29931544e403069576fd1a4865bb8de
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

<<<<<<< HEAD
    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(arg)
        objdict = storage.all()
=======
    def do_update(self, arg):
        """
        Updates an instance based on the class name and id.
        """
        argl = parse(arg)
        objd = storage.all()
>>>>>>> c87e3fc5b29931544e403069576fd1a4865bb8de

        if len(argl) == 0:
            print("** class name missing **")
            return False
<<<<<<< HEAD
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
=======
=======
            print(["{}".format(str(v))
                  for _, v in all_objs.items() if type(v).__name__ == args[0]])
            return
=======
        Checking if stdin user typed class name and id
        """
        if len(name) == 0:
            print("** class name missing **")
            return False
        else:
            return True

    def check_class_id(self, name=""):
        """
        Checking class id
        """
        if len(name.split(' ')) == 1:
            print("** instance id missing **")
            return False
        else:
            return True
>>>>>>> 5b613d50bb0fbaeaac59b32c00c4a33c1b3e813d

    def found_class_name(self, name=""):
        """
<<<<<<< HEAD
        args = arg.split(maxsplit=3)
        if not validate_classname(args, check_id=True):
            return

        instance_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return

        match_json = re.findall(r"{.*}", arg)
        if match_json:
            payload = None
            try:
                payload: dict = json.loads(match_json[0])
            except Exception:
                print("** invalid syntax")
                return
            for k, v in payload.items():
                setattr(req_instance, k, v)
            storage.save()
            return
        if not validate_attrs(args):
            return
        first_attr = re.findall(r"^[\"\'](.*?)[\"\']", args[3])
        if first_attr:
            setattr(req_instance, args[2], first_attr[0])
        else:
            value_list = args[3].split()
            setattr(req_instance, args[2], parse_str(value_list[0]))
        storage.save()
>>>>>>> a117c8d72be540ce70134bcadf324a2292836c3e


def validate_classname(args, check_id=False):
    """Runs checks on args to validate classname entry.
    """
    if len(args) < 1:
        print("** class name missing **")
        return False
    if args[0] not in current_classes.keys():
        print("** class doesn't exist **")
        return False
    if len(args) < 2 and check_id:
        print("** instance id missing **")
        return False
    return True


def validate_attrs(args):
    """Runs checks on args to validate classname attributes and values.
    """
    if len(args) < 3:
        print("** attribute name missing **")
        return False
    if len(args) < 4:
        print("** value missing **")
        return False
    return True

<<<<<<< HEAD
>>>>>>> c87e3fc5b29931544e403069576fd1a4865bb8de
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
<<<<<<< HEAD
            obj = objdict["{}.{}".format(argl[0], argl[1])]
=======
            obj = objd["{}.{}".format(argl[0], argl[1])]

>>>>>>> c87e3fc5b29931544e403069576fd1a4865bb8de
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
<<<<<<< HEAD
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
=======
            obj = objd["{}.{}".format(argl[0], argl[1])]

            for index, jndex in eval(argl[2]).items():
                if (index in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[index]) in
                        {str, int, float}):
                    valtype = type(obj.__class__.__dict__[index])
                    obj.__dict__[jndex] = valtype(jndex)
                else:
                    obj.__dict__[index] = jndex
        storage.save()
=======

def is_float(x):
    """Checks if `x` is float.
    """
    try:
        a = float(x)
    except (TypeError, ValueError):
        return False
    else:
=======
        Finding the name class
        """
        if self.check_class_name(name):
            args = shlex.split(name)
            if args[0] in HBNBCommand.__classes:
                if self.check_class_id(name):
                    key = args[0] + '.' + args[1]
                    return key
                else:
                    print("** class doesn't exist **")
                    return None

    def do_quit(self, args):
        '''
        Quiting command to exit that program
        '''
>>>>>>> 5b613d50bb0fbaeaac59b32c00c4a33c1b3e813d
        return True

    def do_EOF(self, args):
        '''
        Handles end of file
        '''
        return True

<<<<<<< HEAD
def is_int(x):
    """Checks if `x` is int.
    """
    try:
        a = float(x)
        b = int(a)
    except (TypeError, ValueError):
        return False
    else:
        return a == b

>>>>>>> a117c8d72be540ce70134bcadf324a2292836c3e

def parse_str(arg):
    """Parse `arg` to an `int`, `float` or `string`.
    """
    parsed = re.sub("\"", "", arg)

    if is_int(parsed):
        return int(parsed)
    elif is_float(parsed):
        return float(parsed)
    else:
        return arg


<<<<<<< HEAD
if __name__ == '__main__':
>>>>>>> c87e3fc5b29931544e403069576fd1a4865bb8de
=======
if __name__ == "__main__":
>>>>>>> a117c8d72be540ce70134bcadf324a2292836c3e
=======
    def emptyline(self):
        '''
        Don't execute anything when the user presses
        '''
        pass


if __name__ == '__main__':
>>>>>>> 5b613d50bb0fbaeaac59b32c00c4a33c1b3e813d
    HBNBCommand().cmdloop()
