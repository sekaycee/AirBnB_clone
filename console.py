#!/usr/bin/python3
''' Enter the command interpreter '''
import shlex
from cmd import Cmd
from models import storage

# list of classes in models directory
clist = storage.models


class HBNBCommand(Cmd):
    ''' Begin command processing '''

    # public class attributes
    prompt = '(hbnb) '

    def do_quit(self, line):
        ''' Quit command to exit the command interpreter '''
        return True

    def do_EOF(self, line):
        ''' EOF command to exit the command interpreter '''
        return True

    def emptyline(self):
        ''' Do nothing when an empty line is passed to the CI '''
        pass

    def do_create(self, args):
        ''' Create an instance of Model given its name eg.
        $ create ModelName
        Throw an Error if ModelName is missing or doesn't exist
        '''
        args, n = parse(args)

        if not n:
            print("** class name missing **")
        elif args[0] not in clist:
            print("** class doesn't exist **")
        elif n == 1:
            tmp = eval(args[0])()
            print(tmp.id)
            tmp.save()
        else:
            print("** Too many arguments for create **")
            pass

    def do_show(self, arg):
        ''' Show an Instance of Model base on its ModelName and id eg.
        $ show MyModel instance_id
        Print error message if either MyModel or instance_id is missing
        Print an Error message for wrong MyModel or instance_id
        '''
        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            try:
                obj = storage.get_by_id(*args)
                print(obj)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** too many arguments for show **")
            pass

    def do_destroy(self, arg):
        ''' Delete an Instance of Model base on its ModelName and id eg.
        $ destroy MyModel instance_id
        Print error message if either MyModel or instance_id is missing
        Print an Error message for wrong MyModel or instance_id
        '''
        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            try:
                storage.remove_by_id(*args)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** too many argument for destroy **")
            pass

    def do_all(self, args):
        ''' Retrieve all instances: eg.
        $ all
        $ all MyModel
        if MyModel is passed returns only instances of MyModel
        '''
        args, n = parse(args)

        if n < 2:
            try:
                print(storage.get_all(*args))
            except ModelNotFoundError:
                print("** class doesn't exist **")
        else:
            print("** Too many argument for all **")
            pass

    def do_update(self, arg):
        ''' Update an instance base on its id eg.
        $ update Model id field value
        Print errors for missing arguments
        '''
        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            print("** attribute name missing **")
        elif n == 3:
            print("** value missing **")
        else:
            try:
                storage.edit_one(*args[0:4])
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")


def parse(line: str):
    ''' Split a line by spaces '''
    args = shlex.split(line)
    return args, len(args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
