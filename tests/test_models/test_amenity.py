#!/usr/bin/python3
"""This module tests class amenity """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """This class defines a test for an amenity """

    def __init__(self, *args, **kwargs):
        """This method initializes a test instance """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ This method tests the name field"""
        new = self.value()
        self.assertEqual(type(new.name), str)
