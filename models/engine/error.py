#!/usr/bin/python3
''' Define the customer errors used in File Storage '''


class ModelNotFoundError(Exception):
    ''' Raise when an unknown module is passed '''
    def __init__(self, arg="BaseModel"):
        super().__init__(f"Model with name {arg} is not registered!")


class InstanceNotFoundError(Exception):
    ''' Raise when an unknown id  is passed '''

    def __init__(self, obj_id="", mod="BaseModel"):
        super().__init__(
                f"Instance of {mod} with id {obj_id} does not exist!")
