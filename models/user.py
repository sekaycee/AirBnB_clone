#!/usr/bin/python3
""" Define class User that inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ Representation of a user """

    # public class attributes
    email = ""
    password = ""
    first_name = ""
    last_name = ""
