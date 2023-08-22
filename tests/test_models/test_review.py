#!/usr/bin/python3
""" Module for testing review """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import unittest


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


class TestReview2(unittest.TestCase):
    """TestReview Class"""
    def setUp(self):
        """Sets up Review for testing"""
        self.review = Review()

    def test_review_type(self):
        """Tests review type"""
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.text), str)

    def test_review_place_id(self):
        """Tests review place_id"""
        self.assertEqual(self.review.place_id, "")

    def test_review_user_id(self):
        """Tests review user_id"""
        self.assertEqual(self.review.user_id, "")

    def test_review_text(self):
        """Tests review text"""
        self.assertEqual(self.review.text, "")

    def test_review_id(self):
        """Tests review id"""
        self.assertEqual(type(self.review.id), str)

    def test_review_created_at(self):
        """Tests review created_at"""
        self.assertEqual(type(self.review.created_at).__name__, "datetime")

    def test_review_updated_at(self):
        """Tests review updated_at"""
        self.assertEqual(type(self.review.updated_at).__name__, "datetime")

    def test_review_str(self):
        """Tests review __str__"""
        self.assertEqual(type(self.review.__str__()), str)

    def test_review_save(self):
        """Tests review save"""
        self.review.save()
        self.assertEqual(type(self.review.updated_at).__name__, "datetime")

    def test_review_to_dict(self):
        """Tests review to_dict"""
        self.assertEqual(type(self.review.to_dict()), dict)

    # def test_review_kwargs(self):
    #     """Tests review kwargs"""
    #     self.new_review = Review(text="Great place")
    #     self.assertEqual(type(self.new_review).__name__, "Review")
    #     self.assertTrue(hasattr(self.new_review, "text"))
    #     self.assertEqual(self.new_review.text, "Great place")
