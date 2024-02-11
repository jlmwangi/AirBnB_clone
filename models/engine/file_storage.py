<<<<<<< HEAD
import json

class FileStorage:
    """Handles serialization and deserialization of objects to/from JSON"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(json_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file exists)"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                json_dict = json.load(file)
                for key, value in json_dict.items():
                    class_name, obj_id = key.split(".")
                    module_name = "models." + class_name
                    cls = eval(module_name + "." + class_name)
                    FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

#======
#!/usr/bin/python3
#mport json


#lass FileStorage:
#   """serializes instances to and from a JSON file"""
#   def __init__(self):
#       """initializes class file storage"""
#       self.__file_path = "data.json"
#       self.__objects = {}

#   def all(self):
#       """returns the dictionary __objects"""
#       return self.__objects

#   def new(self, obj):
#       """sets in dict, the obj with key <obj class name>.id"""
#       key = "{}.{}".format(obj.__class__.__name__, obj.id)
#       self.__objects[key] = obj.to_dict()

#   def save(self):
#       """serializes __objects to JSON file"""
#       from models.base_model import BaseModel
#       from models.user import User

#       serialized = {}

#       for obj_key, obj_val in self.__objects.items():
#           obj_class_name, obj_id = obj_key.split('.')
#           if obj_class_name == 'BaseModel':
#               obj = BaseModel(**obj_val)
#           elif obj_class_name == 'User':
#               obj = User(**obj_val)
#           else:
#               continue
#           serialized[obj_key] = obj.to_dict()

#       with open(self.__file_path, 'w') as file:
#           json.dump(serialized, file)

#   def reload(self):
#       """deserializes the JSON file"""
#       try:
#           with open(self.__file_path, 'r') as file:
#               self.__objects = json.load(file)
#       except FileNotFoundError:
#           pass
#>>>>>> d57d05e9dd089ebbda7c7569681f241342a34fa9
