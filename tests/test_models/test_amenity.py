#!/usr/bin/python3
""" Module for testing amenity """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import unittest
from os import getenv


class test_Amenity(test_basemodel):
    """ Test Cases for Amenity Class """

    def __init__(self, *args, **kwargs):
        """ Initialize Amenity Class """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Test Amenity Name """
        new = self.value()
        self.assertEqual(type(new.name), str)


class TestAmenity2(unittest.TestCase):
    """TestAmenity Class"""
    def setUp(self):
        """Sets up Amenity for testing"""
        self.amenity = Amenity()

    def test_amenity_type(self):
        """Tests amenity type"""
        self.assertEqual(type(self.amenity.name), str)

    def test_amenity_name(self):
        """Tests amenity name"""
        self.assertEqual(self.amenity.name, "")

    def test_amenity_id(self):
        """Tests amenity id"""
        self.assertEqual(type(self.amenity.id), str)

    def test_amenity_created_at(self):
        """Tests amenity created_at"""
        self.assertEqual(type(self.amenity.created_at).__name__, "datetime")

    def test_amenity_updated_at(self):
        """Tests amenity updated_at"""
        self.assertEqual(type(self.amenity.updated_at).__name__, "datetime")

    def test_amenity_str(self):
        """Tests amenity __str__"""
        self.assertEqual(type(self.amenity.__str__()), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_amenity_save(self):
        """Tests amenity save"""
        self.amenity.save()
        self.assertEqual(type(self.amenity.updated_at).__name__, "datetime")

    def test_amenity_to_dict(self):
        """Tests amenity to_dict"""
        self.assertEqual(type(self.amenity.to_dict()), dict)

    def test_amenity_kwargs(self):
        """Tests amenity kwargs"""
        self.new_amenity = Amenity(name="Wifi")
        self.assertEqual(type(self.new_amenity).__name__, "Amenity")
        self.assertTrue(hasattr(self.new_amenity, "name"))
        self.assertEqual(self.new_amenity.name, "Wifi")
