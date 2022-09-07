#!/usr/bin/python3
"""
This module contains tests base_model
"""
import unittest
from datetime import datetime

from models.base_model import BaseModel


class MyTestCase(unittest.TestCase):
    """A class that tests the base_model class
    """
    def setUp(self):
        """Create an instance to be used across methods
        """
        self.my_model = BaseModel()

    def test_everything(self):
        """Method that tests everything
        """
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89
        print(self.my_model.id)
        print(self.my_model)
        print(type(self.my_model.created_at))
        print("--")
        my_model_json = self.my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(key,
                                           type(my_model_json[key]),
                                           my_model_json[key]))

        print("--")
        my_new_model = BaseModel(**my_model_json)
        print(my_new_model.id)
        print(my_new_model)
        print(type(my_new_model.created_at))

        print("--")
        print(self.my_model is my_new_model)

    def test_attribute_id(self):
        """Method that tests attributes
        """
        self.assertEqual(self.my_model.id,
                         self.my_model.to_dict().__getitem__('id'))

    def test_type_created_at(self):
        """Method to test type of attribute
        created at
        """
        self.assertIsInstance(self.my_model.created_at, datetime)

    def test_is_my_model(self):
        """Method to test whether two instances are different
        """
        my_model_json = self.my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertFalse(self.my_model is my_new_model, False)


if __name__ == '__main__':
    unittest.main()
