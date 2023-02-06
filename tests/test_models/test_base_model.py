#!/usr/bin/python3
''' Define unittests for models/base_model.py.
Unittest classes:
    TestBaseModel_Instance
    TestBaseModel_Save
    TestBaseModel_To_Dict
'''
import os
import models
import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    ''' Testing instance(s) of the BaseModel class. '''

