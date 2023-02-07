#!/usr/bin/python3
''' Module contain class that serializes instances to a JSON file
and deserializes JSON file to instances
'''
import json


class FileStorage:
    ''' Serializes and deserializes JSON objects '''
    # private class attributes
    __file_path = "file.json"
    __objects = {}

    # public instance methods
    def all(self):
        ''' Return dictionary __objects '''
        Return (FileStorage.__objects)

    def new(self, obj):
        ''' Set in __objects the obj with key <obj class name >.id '''
        key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        ''' Serialize __objects to the JSON file '''
        s_dict = {
            key: val.to_dict() for key, val in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(s_dict, f)

    def reload(self):
        ''' Deserialize __objects from the JSON file '''
        try:
            d_dict = {}
            with open(FileStorage.__file_path, 'r') as f:
                d_dict = json.load(f.read())
            FileStorage.__objects = {
                key: eval(obj['__class__'])(**obj)
                    for key, obj in d_dict.items()}
        except (FileNotFoundError, JSONDecodeError):
            # no need for error
            pass
