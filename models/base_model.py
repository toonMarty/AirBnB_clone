#!/usr/bin/python3
"""
This module contains a class BaseModel that defines
all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """A class that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        This method initializes BaseModels instances
        """
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """
        This method returns a string of the instance
        Returns:
             str: a string representation of the instance
        """
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """
        This method updates the public instance attribute updated_at with
        the current datetime
        """
        from models import storage
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
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary
