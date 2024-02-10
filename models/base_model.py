#!/usr/bin/python3
import datetime
import uuid
from engine import file_storage
from file_storage import storage


class BaseModel():
    """defines all common attributes for other classes"""

    def __init__(self, *args, **kwargs):
        """initializes class base model"""
        if kwargs:
            self.my_number = kwargs.get('my_number')
            self.name = kwargs.get('name')
            self.created_at = kwargs.get('created_at', datetime.datetime.now())
            self.updated_at = kwargs.get('updated_at', datetime.datetime.now())
            self.id = kwargs.get('id', str(uuid.uuid4()))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

        if isinstance(storage, FileStorage) and id not in kwargs:
            storage.new(self)

    def __str__(self):
        """prints string representation of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates updated_at with current datetime"""
        self.updated_at = datetime.datetime.now()
        storage.new(self)

    def to_dict(self):
        """returns a dict containing all key/values of the instance"""
        return {
                'my_number': self.my_number,
                'name': self.name,
                '__class__': self.__class__.__name__,
                'created_at': self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'updated_at': self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'id': self.id
                }
