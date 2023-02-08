#!/usr/bin/python3
''' Define unittests for models/engine/file_storage.py.
Unittest classes:
    TestFileStorage_Instance
    TestFileStorage_Methods
'''
import os
import json
import unittest
from models import storage
from models.city import City
from models.user import User
from datetime import datetime
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_Instance(unittest.TestCase):
    ''' Test instantiation of the FileStorage class '''

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(storage), FileStorage)


class TestFileStorage_Methods(unittest.TestCase):
    ''' Test methods of the FileStorage class '''

    @classmethod
    def setUp(self):
        try:
            os.rename('file.json', 'tmp')
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove('file.json')
        except IOError:
            pass
        try:
            os.rename('tmp', 'file.json')
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def t_helper(self):
        m_dict = { 'bm': BaseModel(), 'us': User(), 'st': State()
            , 'pl': Place(), 'cy': City(), 'am': Amenity(), 'rv': Review() }
        storage.new(m_dict['bm'])
        storage.new(m_dict['us'])
        storage.new(m_dict['st'])
        storage.new(m_dict['pl'])
        storage.new(m_dict['cy'])
        storage.new(m_dict['am'])
        storage.new(m_dict['rv'])
        return (m_dict)

    def test_all(self):
        self.assertEqual(dict, type(storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new(self):
        m_dict = self.t_helper()
        self.assertIn('BaseModel.' + m_dict['bm'].id, storage.all().keys())
        self.assertIn(m_dict['bm'], storage.all().values())
        self.assertIn('User.' + m_dict['us'].id, storage.all().keys())
        self.assertIn(m_dict['us'], storage.all().values())
        self.assertIn('State.' + m_dict['st'].id, storage.all().keys())
        self.assertIn(m_dict['st'], storage.all().values())
        self.assertIn('Place.' + m_dict['pl'].id, storage.all().keys())
        self.assertIn(m_dict['pl'], storage.all().values())
        self.assertIn('City.' + m_dict['cy'].id, storage.all().keys())
        self.assertIn(m_dict['cy'], storage.all().values())
        self.assertIn('Amenity.' + m_dict['am'].id, storage.all().keys())
        self.assertIn(m_dict['am'], storage.all().values())
        self.assertIn('Review.' + m_dict['rv'].id, storage.all().keys())
        self.assertIn(m_dict['rv'], storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

    def test_save(self):
        m_dict = self.t_helper()
        storage.save()
        save_text = ''
        with open('file.json', 'r') as f:
            save_text = f.read()
            self.assertIn('BaseModel.' + m_dict['bm'].id, save_text)
            self.assertIn('User.' + m_dict['us'].id, save_text)
            self.assertIn('State.' + m_dict['st'].id, save_text)
            self.assertIn('Place.' + m_dict['pl'].id, save_text)
            self.assertIn('City.' + m_dict['cy'].id, save_text)
            self.assertIn('Amenity.' + m_dict['am'].id, save_text)
            self.assertIn('Review.' + m_dict['rv'].id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload(self):
        m_dict = self.t_helper()
        storage.save()
        storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn('BaseModel.' + m_dict['bm'].id, objs)
        self.assertIn('User.' + m_dict['us'].id, objs)
        self.assertIn('State.' + m_dict['st'].id, objs)
        self.assertIn('Place.' + m_dict['pl'].id, objs)
        self.assertIn('City.' + m_dict['cy'].id, objs)
        self.assertIn('Amenity.' + m_dict['am'].id, objs)
        self.assertIn('Review.' + m_dict['rv'].id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == '__main__':
    unittest.main()
