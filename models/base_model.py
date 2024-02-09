#!/usr/bin/python3
import datetime
import uuid


class BaseModel():
    """defines all common attributes for other classes"""

    def __init__(self):
        """initializes class base model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """prints string representation of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates updated_at with current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dict containing all key/values of the instance"""
        return {
                '__class__': self.__class__.__name__,
                'created_at': str(self.created_at.isoformat("T")),
                'updated_at': str(self.updated_at.isoformat("T"))
                'id': self.id
                }
