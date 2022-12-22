#!/usr/bin/python3
""" This module contains a test for the review class"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ This class defines a test for a review"""

    def __init__(self, *args, **kwargs):
        """ Initilalizes a review test instance """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ This method tests the place id """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ This method tests user id """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ This method tests the review description """
        new = self.value()
        self.assertEqual(type(new.text), str)
