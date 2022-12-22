#!/usr/bin/python3
""" This module contains a test for the class User"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Class that defines test class for class User"""

    def __init__(self, *args, **kwargs):
        """ Initializes the test instance"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Method that tests the first name"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Method that tests the last name"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Method that tests the email"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Method that tests the password"""
        new = self.value()
        self.assertEqual(type(new.password), str)
