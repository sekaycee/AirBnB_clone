#!/usr/bin/python3
''' Enter the command interpreter '''
import cmd


class HBNBCommand(cmd.Cmd):
    ''' Begin command processing '''

    # public class attributes
    prompt = "(hbnb) "
    def do_quit(self, line):
        ''' Quit command to exit the command interpreter '''
        return True

    def do_EOF(self, line):
        ''' EOF command to exit the command interpreter '''
        return True

    def emptyline(self):
        ''' Do nothing when an empty line is passed to the CI'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
