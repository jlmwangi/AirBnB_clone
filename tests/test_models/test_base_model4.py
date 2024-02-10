#!/usr/bin/python3

import uuid
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """tests base_model defining common attributes for classes"""
    def test_unique_id(self):
        """tests whether the id entered is unique"""
        ob1 = BaseModel()
        ob2 = BaseModel()
        self.assertNotEqual(ob1.id, ob2.id)

    def test_current_datetime(self):
        """tests whether datetime upon creation is current"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertAlmostEqual(obj1.created_at, obj2.created_at, delta=datetime.timedelta(seconds=2)))

    def test_not_strings(self):
        """tests whether created_at and updated_at times are not strings"""
        obj1 = BaseModel()
        self.assertIsInstance(obj1.created_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
