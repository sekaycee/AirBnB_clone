#!/usr/bin/python3
''' Module serializes and deserializes instances to/from a JSON file '''
import os
import json


class FileStorage:
    ''' Serializes and deserializes JSON objects '''
    # private class attributes
    __file_path = "file.json"
    __objects = {}

    # constructor method
    def __init__(self):
        ''' Constructor for the class '''
        pass

    # public instance methods
    def all(self):
        ''' Return dictionary __objects '''
        return (FileStorage.__objects)

    def new(self, obj):
        ''' Set in __objects the obj with key <obj class name >.id '''
        key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        ''' Serialize __objects to the JSON file '''
        s_dict = {}
        for key, val in FileStorage.__objects.items():
            s_dict[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(s_dict, f)

    def reload(self):
        ''' Deserialize __objects from the JSON file '''
        from models.base_model import BaseModel

        d_dict = {'BaseModel': BaseModel}
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, val in json.load(f).items():
                    self.new(d_dict[val['__class__']](**val))
