#!/usr/bin/python3
''' BaseModel module.. form the baseclass for other project models '''

from uuid import uuid4
from models import storage
from datetime import datetime


class BaseModel:
    ''' Define all common attributes/methods '''
    def __init__(self, *args, **kwargs):
        ''' Deserialize a serialized class or initialize a new one '''
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
    
    def __str__(self):
        ''' Override default implementation of __str__ method '''
        fmt = '[{}] ({}) {}'
        return (fmt.format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        ''' Update `self.updated_at` with the current datetime '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' Return a new dictionary with key and strformatted datetime '''
        new_dict = {}
        for key, values in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                new_dict[key] = values.strftime('%Y-%m-%dT%H:%M:%S.%f')
        new_dict['__class__'] = type(self).__name__
        return (new_dict)
