#!/usr/bin/python3
"""
This module contains tests for the BaseModel class
"""
import unittest
from models.base_model import BaseModel


class MyTestCase(unittest.TestCase):
    """A class which defines test methods
    """
    def setUp(self):
        """
        Set up class instances
        """
        self.my_model = BaseModel()
        self.my_model2 = BaseModel()

    def test_base_attributes(self):
        """
        Method that tests attributes
        """
        self.my_model.name = "My First Model"
        self.my_model.my_number = 32
        self.my_model.age = 14
        print(self.my_model)
        self.my_model.save()
        print(self.my_model)

    def test_save(self):
        """
        Testing the save method
        """
        self.my_model.save()
        print(self.my_model)

    def test_to_dict(self):
        """
        Testing the to_dict() method
        """
        self.my_model_json = self.my_model.to_dict()
        print(self.my_model_json)

    def test_time_format(self):
        """
        Testing iso format for time
        """
        self.assertEqual(self.my_model.created_at.isoformat(),
                         self.my_model.created_at.isoformat())
        self.assertEqual(self.my_model.updated_at.isoformat(),
                         self.my_model.updated_at.isoformat())

    def test_not_equal_uuid(self):
        """
        Testing ids for two different instances
        """
        self.assertNotEqual(self.my_model.id, self.my_model.id)


if __name__ == '__main__':
    unittest.main()
