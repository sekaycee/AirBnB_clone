#!/usr/bin/python3
''' Define unittests for models/amenity.py.
Unittest classes:
    TestAmenity_Instance
    TestAmenity_Save
    TestAmenity_To_Dict
'''
import os
import models
import unittest
from time import sleep
from datetime import datetime
from models.amenity import Amenity


class TestAmenity_Instance(unittest.TestCase):
    ''' Test instantiation of the Amenity class '''

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_is_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_is_id_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_is_created_at_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_is_updated_at_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_is_name_public_class_attribute(self):
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn('name', dir(Amenity()))
        self.assertNotIn('name', am.__dict__)

    def test_two_amenities_unique_ids(self):
        f_am = Amenity()
        s_am = Amenity()
        self.assertNotEqual(f_am.id, s_am.id)

    def test_two_amenities_different_created_at(self):
        f_am = Amenity()
        sleep(0.05)
        s_am = Amenity()
        self.assertLess(f_am.created_at, s_am.created_at)

    def test_two_amenities_different_updated_at(self):
        f_am = Amenity()
        sleep(0.05)
        s_am = Amenity()
        self.assertLess(f_am.updated_at, s_am.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        am = Amenity()
        am.id = '123456'
        am.created_at = am.updated_at = dt
        am_str = am.__str__()
        self.assertIn('[Amenity] (123456)', am_str)
        self.assertIn('"id": "123456"', am_str)
        self.assertIn('"created_at": ' + dt_repr, am_str)
        self.assertIn('"updated_at": ' + dt_repr, am_str)

    def test_args_unused(self):
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    def test_instantiation_with_kwargs(self):
        ''' Instantiate with kwargs test method '''
        dt = datetime.today()
        dt_iso = dt.isoformat()
        am = Amenity(id='345', created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(am.id, '345')
        self.assertEqual(am.created_at, dt)
        self.assertEqual(am.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_Save(unittest.TestCase):
    ''' Test save method of the Amenity class '''

    @classmethod
    def setUp(self):
        try:
            os.rename('file.json', 'tmp')
        except IOError:
            pass

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
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        self.assertLess(first_updated_at, am.updated_at)

    def test_two_saves(self):
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        second_updated_at = am.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        am.save()
        self.assertLess(second_updated_at, am.updated_at)

    def test_save_with_arg(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)

    def test_save_updates_file(self):
        am = Amenity()
        am.save()
        amid = 'Amenity.' + am.id
        with open('file.json', 'r') as f:
            self.assertIn(amid, f.read())


class TestAmenity_To_Dict(unittest.TestCase):
    ''' Test to_dict method of the Amenity class '''

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        am = Amenity()
        self.assertIn('id', am.to_dict())
        self.assertIn('created_at', am.to_dict())
        self.assertIn('updated_at', am.to_dict())
        self.assertIn('__class__', am.to_dict())

    def test_to_dict_contains_added_attributes(self):
        am = Amenity()
        am.middle_name = 'Caleb'
        am.number = 98
        self.assertEqual('Caleb', am.middle_name)
        self.assertIn('number', am.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        am = Amenity()
        am_dict = am.to_dict()
        self.assertEqual(str, type(am_dict['id']))
        self.assertEqual(str, type(am_dict['created_at']))
        self.assertEqual(str, type(am_dict['updated_at']))

    def test_to_dict_output(self):
        dt = datetime.today()
        am = Amenity()
        am.id = '123456'
        am.created_at = am.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(am.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        am = Amenity()
        self.assertNotEqual(am.to_dict(), am.__dict__)

    def test_to_dict_with_arg(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.to_dict(None)


if __name__ == '__main__':
    unittest.main()
