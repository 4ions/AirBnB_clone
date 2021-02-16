#!/usr/bin/python3
"""import modules"""
import json
import os
"""module of FileStorage"""


class FileStorage:
    """ class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return all objects in dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets new objects in dictionary """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes the dictionary to json """
        my_dict = {}
        with open(FileStorage.__file_path, "w") as f:
            for key, item in FileStorage.__objects.items():
                my_dict[key] = item.to_dict()
            json.dump(my_dict, f)

    def reload(self):
        """ Deserializes json into a __objects """
        try:
            with open(FileStorage.__file_path, "r") as f:

                from models.base_model import BaseModel
                from models.user import User
                from models.amenity import Amenity
                from models.city import City
                from models.place import Place
                from models.state import State
                from models.review import Review

                test = json.load(f)
            for key, item in test.items():
                self.__objects[key] = eval(item["__class__"])(**item)
        except IOError:
            pass
