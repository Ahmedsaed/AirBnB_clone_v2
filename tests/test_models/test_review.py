#!/usr/bin/python3
""" Module for testing review """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Test Cases for Review Class """

    def __init__(self, *args, **kwargs):
        """ Initialize Review Class """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Test Place ID """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Test User ID """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Test Text """
        new = self.value()
        self.assertEqual(type(new.text), str)
