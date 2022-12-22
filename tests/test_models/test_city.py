#!/usr/bin/python3
"""This module tests class City """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """This is a test class for City """

    def __init__(self, *args, **kwargs):
        """Initialize test object """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ This method tests the id of a state"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ This method tests the name of a city"""
        new = self.value()
        self.assertEqual(type(new.name), str)
