#!/usr/bin/python3
""" console """

import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models import storage

"""after of import"""


class HBNBCommand(cmd.Cmd):
    """
    cmd class run command line
    """
    class_list = ['BaseModel', 'User', 'Amenty',
                  'City', 'Place', 'State', 'Review']
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Quit command to exit the program
         """
        print()
        return True

    def do_EOF(self, line):
        """
        EFO """
        print()
        return True

    def do_create(self, line):
        """create a new instance of class"""
        if line == "":
            print("** class name missing **")
        else:
            try:
                new_base = eval(line)()
                print(new_base.id)
                new_base.save()
            except:
                print("** class doesnt exist **")

    def do_show(self, line):
        """ Prints the string representation
        of an instance based on the class name and
        id
        """

        if line == "":
            print("** class name missing **")
        else:
            my_line = line.split()
            if my_line[0] not in self.class_list:
                print("** class doesn't exist **")
            elif len(my_line) != 2:
                print("** instance id missing **")
            else:
                try:
                    key = "{}.{}".format(my_line[0], my_line[1])
                    all_objs = storage.all()
                    obj = all_objs[key]
                    print(obj)
                except:
                    print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based
        on the class name and id"""
        if line == "":
            print("** class name missing **")
            return
        else:
            my_line = line.split()
            if my_line[0] not in self.class_list:
                print("** class doesn't exist **")
                return
            elif len(my_line) != 2:
                print("** instance id missing **")
                return
            else:
                try:
                    key = "{}.{}".format(my_line[0], my_line[1])
                    obj = storage.all()
                    obj.pop(key)
                    storage.save()

                except:
                    print("** no instance found **")

    def do_all(self, line):
        """print all in file file.json"""
        all_obj = storage.all()
        my_list = []
        if line in self.class_list:
            for key, obj in all_obj.items():
                if line in key:
                    print(obj)
                    my_list.append(obj)
            print(my_list)
        elif line == "":
            for obj in all_obj.values():
                my_list.append(obj)
            print(my_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """update a class"""
        if line == "":
            print("** class name missing **")
            return
        my_line = line.split()
        all_objs = storage.all()
        if my_line[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        if len(my_line) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(my_line[0], my_line[1])
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(my_line) < 3:
            print("** attribute name missing **")
            return
        if len(my_line) < 4:
            print("** value missing **")
            return
        obj = all_objs[key]
        atr = my_line[2]
        setattr(obj, atr, my_line[3])
        all_objs[key].save()

    def do_count(self, line):
        """count number of objs of this class"""
        count = 0
        if line in HBNBCommand.class_list:
            for obj in storage.all().values():
                if line in obj.__class__.__name__:
                    count += 1
            print(count)
        else:
            return

    def default(self, line):
        """retrieve all instances of a clss by using:
        <class name>.funtion()"""
        my_line = line.split(".")
        if my_line[0] in self.class_list:
            try:
                args = my_line[1].split("(")
                if args[0] == "all":
                    HBNBCommand.do_all(self, my_line[0])
                elif args[0] == "count":
                    HBNBCommand.do_count(self, my_line[0])
                elif args[0] == "show":
                    id_class = args[1]
                    HBNBCommand.do_show
                    (self, my_line[0] + " " + id_class[1:-2])
                elif args[0] == "destroy":
                    id_class = args[1]
                    HBNBCommand.do_destroy
                    (self, my_line[0] + " " + id_class[1:-2])
                elif args[0] == "update":
                    paramer = args[1].split(',')
                    id_class = paramer[0].strip('"')
                    dirt = paramer[1].split(':')
                    name_atr = dirt[0].strip(" {'")
                    value_atr = dirt[1].strip(' "})')
                    HBNBCommand.do_update
                    (self, my_line[0] + ' ' + id_class +
                        ' ' + name_atr + ' ' + value_atr)
            except:
                print("*** Unknown syntax:", line)
        else:
            print("*** Unknown syntax:", line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
