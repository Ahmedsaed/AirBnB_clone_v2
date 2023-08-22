#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Test Cases for Place Class """

    def __init__(self, *args, **kwargs):
        """ Test Initialize Place Class """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Test City ID """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ Test User ID """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ Test Place Name """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ Test Place Description """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ Test Number of Rooms """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Test Number of Bathrooms """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Test Max Number of Guests """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Test Price by Night """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Test Latitude """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ Test Longitude """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ Test Amenity IDs """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
