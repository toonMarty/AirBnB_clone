#!/usr/bin/python3
"""This module contains a class that tests the class state """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ This class defines a test for class State"""

    def __init__(self, *args, **kwargs):
        """ Initializes a state test instance"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Method that tests the name of a state"""
        new = self.value()
        self.assertEqual(type(new.name), str)
