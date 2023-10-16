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


    if __name__ == '__main__':
    HBNBCommand().cmdloop()
