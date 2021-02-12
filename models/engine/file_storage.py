#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review

import os


class FileStorage:
    """ class """

    __file_path = "file.json"
    __objects = {}
    
    
    def all(self):
        """ all """
        return FileStorage.__objects

    def new(self, obj):
        """ new """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ save """
        my_dict = {}
        with open(FileStorage.__file_path, "w") as f:
            for key, item in FileStorage.__objects.items():
                my_dict[key] = item.to_dict()
            json.dump(my_dict, f)

    def reload(self):
        """ reaload """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as f:
            test = json.load(f)
        for key, item in test.items():
            self.__objects[key] = eval(item["__class__"])(**item)
