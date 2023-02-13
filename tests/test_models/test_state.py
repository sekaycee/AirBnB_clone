#!/usr/bin/python3
''' Define unittests for models/state.py '''
import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    ''' Test the State class '''

    s = State()

    def test_class_exists(self):
        ''' Test if class exists '''
        res = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.s)), res)

    def test_user_inheritance(self):
        ''' Test if State is a subclass of BaseModel '''
        self.assertIsInstance(self.s, State)

    def testHasAttributes(self):
        ''' Verify if attributes exist '''
        self.assertTrue(hasattr(self.s, 'name'))
        self.assertTrue(hasattr(self.s, 'id'))
        self.assertTrue(hasattr(self.s, 'created_at'))
        self.assertTrue(hasattr(self.s, 'updated_at'))

    def test_types(self):
        ''' Test if the type of the attribute is the correct one '''
        self.assertIsInstance(self.s.name, str)
        self.assertIsInstance(self.s.id, str)
        self.assertIsInstance(self.s.created_at, datetime)
        self.assertIsInstance(self.s.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
