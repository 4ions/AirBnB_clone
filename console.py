#!/usr/bin/python3
""" console """

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):

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
            class_list = ['BaseModel']
            my_line = line.split()
            if my_line[0] not in class_list:
                print("** class doesn't exist **")
            if len(my_line) != 2:
                print("** instance id missing **")
            else:
                try:
                    key = str(my_line[0])+"."+str(my_line[1])
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
        class_list = ['BaseModel']
        my_line = line.split()
        if my_line[0] not in class_list:
            print("** class doesn't exist **")



        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
