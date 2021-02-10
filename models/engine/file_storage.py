#!/usr/bin/python3
import json
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
            new_dict = {}
            new_dict = json.load(f)
            for key, item in new_dict.items():
                FileStorage.__objects[key] = item



