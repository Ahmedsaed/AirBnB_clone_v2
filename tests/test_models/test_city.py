#!/usr/bin/python3
""" Module for testing city """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest
from os import getenv


class test_City(test_basemodel):
    """ Test Cases for City Class """

    def __init__(self, *args, **kwargs):
        """ Initialize City Class """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    # def test_state_id(self):
    #     """ Test State ID """
    #     new = self.value()
    #     self.assertEqual(type(new.state_id), str)

    # def test_name(self):
    #     """ Test City Name """
    #     new = self.value()
    #     self.assertEqual(type(new.name), str)


class TestCity1(unittest.TestCase):
    """TestCity Class"""
    def setUp(self):
        """Sets up City for testing"""
        self.city = City()

    # def test_city_type(self):
    #     """Tests city type"""
    #     self.assertEqual(type(self.city.name), str)

    # def test_city_name(self):
    #     """Tests city name"""
    #     self.assertEqual(self.city.name, "")

    def test_city_id(self):
        """Tests city id"""
        self.assertEqual(type(self.city.id), str)

    def test_city_created_at(self):
        """Tests city created_at"""
        self.assertEqual(type(self.city.created_at).__name__, "datetime")

    def test_city_updated_at(self):
        """Tests city updated_at"""
        self.assertEqual(type(self.city.updated_at).__name__, "datetime")

    def test_city_str(self):
        """Tests city __str__"""
        self.assertEqual(type(self.city.__str__()), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_city_save(self):
        """Tests city save"""
        self.city.save()
        self.assertEqual(type(self.city.updated_at).__name__, "datetime")

    def test_city_to_dict(self):
        """Tests city to_dict"""
        self.assertEqual(type(self.city.to_dict()), dict)

    def test_city_kwargs(self):
        """Tests city kwargs"""
        self.new_city = City(name="San Francisco")
        self.assertEqual(type(self.new_city).__name__, "City")
        self.assertTrue(hasattr(self.new_city, "name"))
        self.assertEqual(self.new_city.name, "San Francisco")
