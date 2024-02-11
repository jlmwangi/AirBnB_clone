#!/usr/bin/python3

import unittest
from engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """tests file storage istances"""
    def setup(self):
        """initialize FileStorage instance"""
        self.storage = FileStorage()
        self.storage.reload()

    def test_initialize(self):
        """check if storage is correctly initialized"""
        self.assertIsInstance(self.storage, FileStorage)
        self.assertEqual(len(self.storage.all()), 0)

    def test_reload_save(self):
        """checks for saved and reloaded data"""
        data = {"key1": "value1", "key2": "value2"}
        self.storage.all().update(data)
        self.storage.save()

        self.storage.reload()
        data_loaded = self.storage.all()
        self.assertEqual(data_loaded, data)

    def test_new_object(self):
        """tests if a new obj is added to storage"""
        ob = {"id": "1", "name": "object1"}
        self.storage.new(ob)
        loaded_ob = self.storage.all()["1"]
        self.assertEqual(loaded_ob, ob)

if __name__ == "__main__":
    unittest.main()
