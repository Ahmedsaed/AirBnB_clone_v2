#!/usr/bin/python3
""" Module for testing place """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import unittest
from os import getenv


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


class TestPlace2(unittest.TestCase):
    """TestPlace Class"""
    def setUp(self):
        """Sets up Place for testing"""
        self.place = Place()

    def test_place_type(self):
        """Tests place type"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_place_name(self):
        """Tests place name"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_place_id(self):
        """Tests place id"""
        self.assertEqual(type(self.place.id), str)

    def test_place_created_at(self):
        """Tests place created_at"""
        self.assertEqual(type(self.place.created_at).__name__, "datetime")

    def test_place_updated_at(self):
        """Tests place updated_at"""
        self.assertEqual(type(self.place.updated_at).__name__, "datetime")

    def test_place_str(self):
        """Tests place __str__"""
        self.assertEqual(type(self.place.__str__()), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_place_save(self):
        """Tests place save"""
        self.place.save()
        self.assertEqual(type(self.place.updated_at).__name__, "datetime")

    def test_place_to_dict(self):
        """Tests place to_dict"""
        self.assertEqual(type(self.place.to_dict()), dict)

    def test_place_kwargs(self):
        """Tests place kwargs"""
        self.new_place = Place(name="San Francisco")
        self.assertEqual(type(self.new_place).__name__, "Place")
        self.assertTrue(hasattr(self.new_place, "name"))
        self.assertEqual(self.new_place.name, "San Francisco")
