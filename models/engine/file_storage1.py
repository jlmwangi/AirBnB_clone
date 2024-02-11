#!/usr/bin/python3
import json


class FileStorage:
    """serializes instances to and from a JSON file"""
    def __init__(self):
        """initializes class file storage"""
        self.__file_path = "data.json"
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in dict, the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to JSON file"""
        from models.base_model import BaseModel
        from models.user import User

        serialized = {}

        for obj_key, obj_val in self.__objects.items():
            obj_class_name, obj_id = obj_key.split('.')
            if obj_class_name == 'BaseModel':
                obj = BaseModel(**obj_val)
            elif obj_class_name == 'User':
                obj = User(**obj_val)
            else:
                continue
            serialized[obj_key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized, file)

    def reload(self):
        """deserializes the JSON file"""
        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass
