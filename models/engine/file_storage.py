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
        return self.__objects

    def new(self, obj):
        """
        (assigns to) __objects the obj with key <obj class name>.id
        Args:
            obj: an instance from another class
        """
        self.__objects[f'{self.__class__.__name__}'] = obj

    def save(self):
        """serializes __objects to the JSON file
        (path: __file_path)
        Returns:
             str: JSON string
        """
        with open(FileStorage.__file_path, mode='w',
                  encoding='utf-8') as f:
            return json.dump(self.__objects, f)

    def reload(self):
        """
         deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file does not exist
        no exception should be raised
        Returns:
             dict: the dictionary __objects
        """
        with open(FileStorage.__file_path, mode='r',
                  encoding='utf-8')as f:
            x = json.load(f)
        return x
