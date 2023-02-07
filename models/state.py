#!/usr/bin/python3
''' Define class State that inherits from BaseModel '''
from models.base_model import BaseModel


class State(BaseModel):
    ''' Representation of state '''
    
    # public class attribute
    name = ''
