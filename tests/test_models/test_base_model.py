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


class TestBaseModel_Instance(unittest.TestCase):
    ''' Test instance(s) of the BaseModel class '''

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_is_id_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_is_created_at_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_is_updated_at_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_is_unique_two_models_ids(self):
        f_bm = BaseModel()
        s_bm = BaseModel()
        self.assertNotEqual(f_bm.id, s_bm.id)

    def test_is__different_two_models_created_at(self):
        f_bm = BaseModel()
        sleep(0.05)
        s_bm = BaseModel()
        self.assertLess(f_bm.created_at, s_bm.created_at)

    def test_is__different_two_models_updated_at(self):
        f_bm = BaseModel()
        sleep(0.05)
        s_bm = BaseModel()
        self.assertLess(f_bm.updated_at, s_bm.updated_at)

    def test_is_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id='345', created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, '345')
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_kwargs_None(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel('12', id='345', created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, '345')
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = '123456'
        bm.created_at = bm.updated_at = dt
        bm_str = bm.__str__()
        self.assertIn('[BaseModel] (123456)', bm_str)
        self.assertIn("'id': '123456'", bm_str)
        self.assertIn("'created_at': " + dt_repr, bm_str)
        self.assertIn("'updated_at': " + dt_repr, bm_str)

    def test_is_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())


class TestBaseModel_Save(unittest.TestCase):
    ''' Test save method of the BaseModel class '''

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

    def test_one_save(self):
        bm = BaseModel()
        updated_at = bm.updated_at
        sleep(0.05)
        bm.save()
        self.assertLess(updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        f_updated_at = bm.updated_at
        sleep(0.05)
        bm.save()
        s_updated_at = bm.updated_at
        sleep(0.05)
        bm.save()
        self.assertLess(f_updated_at, s_updated_at)
        self.assertLess(s_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bm_id = 'BaseModel.' + bm.id
        with open('file.json', 'r') as f:
            self.assertIn(bm_id, f.read())


class TestBaseModel_To_Dict(unittest.TestCase):
    ''' Test to_dict method of the BaseModel class '''

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn('id', bm.to_dict())
        self.assertIn('created_at', bm.to_dict())
        self.assertIn('updated_at', bm.to_dict())
        self.assertIn('__class__', bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = 'Kay Cee'
        bm.number = 92
        self.assertIn('name', bm.to_dict())
        self.assertIn('number', bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict['created_at']))
        self.assertEqual(str, type(bm_dict['updated_at']))

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = '123456'
        bm.created_at = bm.updated_at = dt
        dict_ = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), dict_)

    def test_contrast_to_dict_self_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


if __name__ == '__main__':
    unittest.main()
