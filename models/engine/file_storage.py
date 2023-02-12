#!/usr/bin/python3
''' Module serializes and deserializes instances to/from a JSON file '''
import os
import json
from datetime import datetime


class FileStorage:
    ''' Serializes and deserializes JSON objects '''
    # private class attributes
    __file_path = "file.json"
    __objects = {}
    models = ('BaseModel', 'Amenity', 'City', 'Place', 'Review'
              , 'State', 'User')

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
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        d_dict = {'BaseModel': BaseModel, 'Amenity': Amenity, 'City': City
            , 'Place': Place, 'Review': Review, 'State': State, 'User': User}
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, val in json.load(f).items():
                    self.new(d_dict[val['__class__']](**val))

    ## crud methods to be invoked by the client (web/console)
    def key_helper(self, model, o_id):
        ''' Find and return a key to an element of model by its id '''
        F = FileStorage
        if model not in F.models:
            # invalid model name.. not yet implemented
            raise ModelNotFoundError(model)

        key = model + '.' + o_id
        if key not in F.__objects:
            # invalid id.. not yet implemented
            raise InstanceNotFoundError(o_id, model)
        return (key)

    def get_by_id(self, model, o_id):
        ''' Find and return an element of model by its id '''
        F = FileStorage
        key = self.key_helper(model, o_id)
        return F.__objects[key]

    def remove_by_id(self, model, o_id):
        ''' Find and delete an element of model by its id '''
        F = FileStorage
        key = key_helper(model, o_id)
        del F.__objects[key]
        self.save()

    def get_all(self, model=''):
        ''' Find all instances or instances of given model '''
        F = FileStorage
        if model and model not in F.models:
            raise ModelNotFoundError(model)
        result = []
        for key, val in F.__objects.items():
            if key.startswith(model):
                result.append(str(val))
        return result

    def edit_one(self, model, o_id, field, value):
        ''' Update an instance '''
        F = FileStorage
        key = key_helper(model, o_id)
        if field in ('id', 'updated_at', 'created_at'):
            # not allowed to be updated
            return
        obj = F.__objects[key]
        try:
            # if object has that value.. cast it to its type
            val_t = type(obj.__dict__[field])
            obj.__dict__[field] = val_t(value)
        except KeyError:
            # object doesn't has the field.. assign the value with its type
            obj.__dict__[field] = value
        finally:
            obj.updated_at = datetime.now()
            self.save()

    def edit_by_dict(self, model, o_id, o_dict):
        ''' Update an instance using a dictionary '''
        od = eval(o_dict)
        for k, v in od.items():
            self.edit_one(model, o_id, k, v)
