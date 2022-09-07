#!/usr/bin/python3
"""
This module contains a class BaseModel that defines
all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """A class that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        This method initializes BaseModels instances
        """
        self.id = uuid.uuid4().__str__()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # updated at this point. Question 4
        if len(kwargs) != 0:  # kwargs is not empty
            kwargs.pop('__class__')  # don't add class as an attribute
            self.__dict__ = kwargs

            for key in self.__dict__:
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.isoformat(self.__dict__[key])

        for key in kwargs:
            # self.__dict__ = kwargs
            if key == 'created_at' or key == 'updated_at':
                kwargs[key] = datetime.isoformat(kwargs[key])
        storage.new(str(self.__dict__))

    def __str__(self):
        """
        This method returns a string of the instance
        Returns:
             str: a string representation of the instance
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """
        This method updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()

        # Update for requirement 5
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance by using
        self.__dict__, only instance attributes set will
        be returned a key __class__ is added to this
        dictionary with the class name of the object

        Returns:
             dict: a dictionary
        """
        self.__dict__['__class__'] = self.__class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()

        return self.__dict__
