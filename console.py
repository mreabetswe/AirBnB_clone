#!/usr/bin/python3

"""The HBnB cosole"""

import cmd
from models.base_model import BaseModel
import models
from models import storage
import os
from models.user import User
from re import split
import sys
import json
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models import storage

class HBNBCommand(cmd.Cmd):
    """ Class HBNB to read command """
    prompt = '(hbnb) '
     allowed_classes = {"BaseModel": BaseModel,
                        "User": User,
                        "Amenity": Amenity,
                        "City": City,
                        "Place": Place,
                        "Review": Review,
                        "State": State}

      def do_quit(self, arg):
        """exit the program"""
        return True

      def do_EOF(self, arg):
        """End of file"""
        print()
        return True

class HBNBCommand(cmd.Cmd):
    """
        HBNBCommand - console class
        @attibutes
            prompt: class attributes - custom prompt
        @methods
            do_quit: quit command
            do_EOF: ctrl-d to quit
            emptyline: do nothing for empty line
    """
    prompt = "(hbnb) "
    my_model = []
    clss = {"BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review}

    def do_create(self, args):
        """creates an instance"""
        if args in type(self).clss.keys():
            mod = type(self).clss[args]()
            mod.save()
            type(self).my_model.append(mod)
            print(mod.id)
        elif args is "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")
        # print("type(self).my_model--->", type(self).my_model)

    def do_show(self, args):
        """shows an instance"""
        argsDelim = args.split()
        if args and argsDelim[0] in type(self).clss.keys():
            if len(argsDelim) < 2:
                print("** instance id missing **")
            else:
                for i in type(self).my_model:
                    if i.id == argsDelim[1]:
                        print(i)
                        break
                else:
                    print("** no instance found **")
        elif args is "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """destroys a created instance"""
        argsDelim = args.split()
        if args and argsDelim[0] in type(self).clss.keys():
            if len(argsDelim) < 2:
                print("** instance id missing **")
            else:
                for i in type(self).my_model:
                    if i.id == argsDelim[1]:
                        type(self).my_model.remove(i)
                        storage.destroy(argsDelim[1])
                        break
                else:
                    print("** no instance found **")
        elif args is "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """prints all instances created"""
        type(self).my_model = list()
        templist = type(self).my_model
        d = storage.all()
        for k, v in d.items():
            templist.append(v)
        if args == "":
            templist.reverse()
            for i in templist:
                print(str(i))
        elif args in type(self).clss.keys():
            temp2 = list()
            for i in templist:
                if type(i) == type(self).clss[args]:
                    temp2.append(str(i))
            temp2.reverse()
            for i in temp2:
                print(i)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """adds attributes to instance"""
        # print(args)
        argsDelim = args.split(" ", 3)
        if args and argsDelim[0] in type(self).clss.keys():
            if len(argsDelim) < 2:
                print("** instance id missing **")
            elif len(argsDelim) < 3:
                print("** attribute name missing **")
            elif len(argsDelim) < 4:
                print("** value missing **")
            else:
                for i in type(self).my_model:
                    if i.id == argsDelim[1]:
                        if '"' in argsDelim[3]:
                            if '"' == argsDelim[3][-1]:
                                value = argsDelim[3].split('"')[0]
                            else:
                                value = argsDelim[3].split('"')[1]
                        elif '.' in argsDelim[3]:
                            value = float(argsDelim[3])
                        else:
                            try:
                                value = int(argsDelim[3])
                            except Exception:
                                value = argsDelim[3]
                        # print("type->", type(value))
                        setattr(i, argsDelim[2], value)
                        i.save()
                        break
                    else:
                        print("** no instance found **")
        elif args is "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_User(self, args):
        """User type object"""
        self.dispatch("User", args)

    def do_Review(self, args):
        """Review type object"""
        self.dispatch("Review", args)

    def do_Amenity(self, args):
        """Amenity type object"""
        self.dispatch("Amenity", args)

    def do_Place(self, args):
        """Place type object"""
        self.dispatch("Place", args)

    def do_State(self, args):
        """State type object"""
        self.dispatch("State", args)

    def do_City(self, args):
        """City type object"""
        self.dispatch("City", args)

    def do_BaseModel(self, args):
        """BaseModel type object"""
        self.dispatch("BaseModel", args)

    def dispatch(self, cls, argv):
        """dispatch Class.func() style calls to the right place"""
        func = argv.split(".")[-1].split("(")[0]
        args = argv.split("(")[-1].split(")")[0].split(", ")
        if func == "all":
            self.do_all(cls)
        elif func == "show":
            self.do_show(cls + " " + args[-1][1:-1])
        elif func == "destroy":
            self.do_destroy(cls + " " + args[-1][1:-1])
        elif func == "update":
            if len(args) != 3:
                print("** too few arguments **")
            arg2 = ""
            for x in args[0:-1]:
                arg2 = arg2 + x[1:-1] + " "
            arg2 = arg2 + args[-1]
            print(arg2)
            self.do_update(cls + " " + arg2)
        elif func == "count":
            ct = 0
            for k, i in storage.all().items():
                if cls in str(i):
                    ct = ct + 1
            print(ct)
        else:
            print("** function doesn't exist **")

    def do_quit(self, args):
        """Quit command to exit the program"""
        storage.save()
        exit()

    def do_EOF(self, args):
        """End Of File :)"""
        storage.save()
        print()
        exit()

    def emptyline(self):
        """Do nothing for empty line"""
        pass

    if __name__ == '__main__':
    HBNBCommand().cmdloop()
