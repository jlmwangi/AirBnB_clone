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

