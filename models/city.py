#!/usr/bin/python
''' Define class City that inherits from BaseModel '''
from models.base_model import BaseModel


class City(BaseModel):
    ''' Representation of city '''

    # public class attributes
    state_id = ''
    name = ''
