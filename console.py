#!/usr/bin/python3
""" console """

import cmd


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Quit """
        return True

    def do_EOF(self, line):
        """ EFO """
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
