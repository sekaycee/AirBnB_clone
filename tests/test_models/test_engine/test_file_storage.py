#!/usr/bin/python3
''' Define unittests for models/engine/file_storage.py '''
import os
import json
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    ''' Test the FileStorage class '''

    my_model = BaseModel()

    def test_class_instance(self):
        ''' Check instance '''
        self.assertIsInstance(storage, FileStorage)

    def test_store_base_model(self):
        ''' Test save and reload functions '''
        self.my_model.full_name = "BaseModel Instance"
        self.my_model.save()
        bm_dict = self.my_model.to_dict()
        all_objs = storage.all()

        key = bm_dict['__class__'] + "." + bm_dict['id']
        self.assertEqual(key in all_objs, True)

    def test_store_base_model_2(self):
        ''' Test save, reload and update functions '''
        self.my_model.my_name = "First name"
        self.my_model.save()
        bm_dict = self.my_model.to_dict()
        all_objs = storage.all()

        key = bm_dict['__class__'] + "." + bm_dict['id']

        self.assertEqual(key in all_objs, True)
        self.assertEqual(bm_dict['my_name'], "First name")

        create1 = bm_dict['created_at']
        update1 = bm_dict['updated_at']

        self.my_model.my_name = "Second name"
        self.my_model.save()
        bm_dict = self.my_model.to_dict()
        all_objs = storage.all()

        self.assertEqual(key in all_objs, True)

        create2 = bm_dict['created_at']
        update2 = bm_dict['updated_at']

        self.assertEqual(create1, create2)
        self.assertNotEqual(update1, update2)
        self.assertEqual(bm_dict['my_name'], "Second name")

    def test_has_attributes(self):
        ''' Verify if attributes exist '''
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def test_save(self):
        ''' Verify if JSON exists '''
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_reload(self):
        ''' Test if reload '''
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        dobj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(dobj, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(dobj[key].to_dict(), value.to_dict())

    def test_save_self(self):
        ''' Check save self '''
        msg = "save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 100)
        self.assertEqual(str(e.exception), msg)

    def test_save_file_storage(self):
        ''' Test if 'new' method is working good '''
        f_var = self.my_model.to_dict()
        new_key = f_var['__class__'] + "." + f_var['id']
        storage.save()
        with open("file.json", 'r') as fd:
            s_var = json.load(fd)
        new = s_var[new_key]
        for key in new:
            self.assertEqual(f_var[key], new[key])


if __name__ == '__main__':
    unittest.main()
