#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


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
