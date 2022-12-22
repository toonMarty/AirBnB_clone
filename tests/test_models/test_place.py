#!/usr/bin/python3
"""This module tests Place attributes """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ This class defines a test for a place"""

    def __init__(self, *args, **kwargs):
        """ This method initializes a test objerc"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ This method tests the city id"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ Method that tests user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ Method that tests the name of a place """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ Method that tests the description of a place"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ Mehod that tests number of rooms"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Method that tests number of bathrooms """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Method that tests the maximum number of guests"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Method that tests price by night """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Method that tests the latitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ Method that tests the longitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ Method that tests the amenity id"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
