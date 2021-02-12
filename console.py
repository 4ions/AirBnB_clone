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

class HBNBCommand(cmd.Cmd):
    class_list = ['BaseModel', 'User', 'Amenty', 'City', 'Place', 'State','Review']
    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Quit command to exit the program
         """
        return True

    def do_EOF(self, line):
        """ EFO """
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
                except:
                    print("** no instance found **")

    def do_all(self, line):
        #aqui va el codigo de cuando no pasan imprimir todo con nombre de clase

        all_obj = storage.all()
        if line in self.class_list:
            for obj_id in all_obj:
                obj = all_obj[obj_id]
                if line == obj.__class__.__name__:
                    print()
                    print(obj)
        elif line == "":
            for obj_id in all_obj:
                obj = all_obj[obj_id]
                print(obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
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


        
        
        
        




if __name__ == '__main__':
    HBNBCommand().cmdloop()
