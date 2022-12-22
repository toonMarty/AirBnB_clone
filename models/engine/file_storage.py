#!/usr/bin/python3
"""
This module contains a class that handles serialization and
deserialization
"""
import json


class FileStorage:
    """Class that defines storage engine
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary __objects
        Returns:
             dict: a dictionary of __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        (assigns to) __objects the obj with key <obj class name>.id
        Args:
            obj: an instance from another class
        """
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """serializes __objects to the JSON file
        (path: __file_path)
        Returns:
             str: JSON string
        """
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """
         deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file does not exist
        no exception should be raised
        Returns:
             dict: the dictionary __objects
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
