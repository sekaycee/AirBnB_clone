#!/usr/bin/python3
''' Define unittests for models/user.py '''
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    ''' Test the User class '''

    u = User()

    def test_class_exists(self):
        ''' Test if class exists '''
        self.assertEqual(str(type(self.u)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        ''' Test if User is a subclass of BaseModel '''
        self.assertIsInstance(self.u, User)

    def testHasAttributes(self):
        ''' Verify if attributes exist '''
        self.assertTrue(hasattr(self.u, 'email'))
        self.assertTrue(hasattr(self.u, 'password'))
        self.assertTrue(hasattr(self.u, 'first_name'))
        self.assertTrue(hasattr(self.u, 'last_name'))
        self.assertTrue(hasattr(self.u, 'id'))
        self.assertTrue(hasattr(self.u, 'created_at'))
        self.assertTrue(hasattr(self.u, 'updated_at'))

    def test_types(self):
        ''' Test if the type of the attribute is the correct one '''
        self.assertIsInstance(self.u.first_name, str)
        self.assertIsInstance(self.u.last_name, str)
        self.assertIsInstance(self.u.email, str)
        self.assertIsInstance(self.u.password, str)
        self.assertIsInstance(self.u.id, str)
        self.assertIsInstance(self.u.created_at, datetime.datetime)
        self.assertIsInstance(self.u.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
