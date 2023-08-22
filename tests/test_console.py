#!/usr/bin/python3
"""Defines unittest cases for console.py.

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import os
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_prompting(unittest.TestCase):
    """Tests for prompting of the HBNB console."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", console.getvalue().strip())


class TestHBNBCommand_help(unittest.TestCase):
    """Tests for help messages of the HBNB console."""
    def test_help_quit(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("help quit"))

    def test_help_create(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("help create"))

    def test_help_EOF(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))

    def test_help_show(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("help show"))

    def test_help_destroy(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))

    def test_help_all(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("help all"))

    def test_help_count(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("help count"))

    def test_help_update(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("help update"))

    def test_help(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("help"))


class TestHBNBCommand_exit(unittest.TestCase):
    """Tests for exiting the HBNB console."""

    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommand_create(unittest.TestCase):
    """Tests for create command of the HBNB console."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_create_missing_class(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_create_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_create_invalid_syntax(self):
        expected = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(expected, console.getvalue().strip())

        expected = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_create_object(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(console.getvalue().strip()))
            test_k = "BaseModel.{}".format(console.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(console.getvalue().strip()))
            test_k = "User.{}".format(console.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(console.getvalue().strip()))
            test_k = "State.{}".format(console.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(console.getvalue().strip()))
            test_k = "City.{}".format(console.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(console.getvalue().strip()))
            test_k = "Amenity.{}".format(console.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(console.getvalue().strip()))
            test_k = "Place.{}".format(console.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(console.getvalue().strip()))
            test_k = "Review.{}".format(console.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())


class TestHBNBCommand_show(unittest.TestCase):
    """Tests for show command of the HBNB console"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_show_missing_class(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_show_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("MyModel.show()"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_show_missing_id_space_notation(self):
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("show User"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("show State"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("show City"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("show Amenity"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("show Place"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("show Review"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_show_missing_id_dot_notation(self):
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show()"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("User.show()"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("State.show()"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("City.show()"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show()"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Place.show()"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Review.show()"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_show_no_instance_found_space_notation(self):
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 1"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("show User 1"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("show State 1"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("show City 1"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("show Amenity 1"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("show Place 1"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("show Review 1"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_show_no_instance_found_dot_notation(self):
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show(1)"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("User.show(1)"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("State.show(1)"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("City.show(1)"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show(1)"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Place.show(1)"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Review.show(1)"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_show_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["BaseModel.{}".format(o_id)]
            command = "show BaseModel {}".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(o.__str__(), console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["User.{}".format(o_id)]
            command = "show User {}".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(o.__str__(), console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["State.{}".format(o_id)]
            command = "show State {}".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(o.__str__(), console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["Place.{}".format(o_id)]
            command = "show Place {}".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(o.__str__(), console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["City.{}".format(o_id)]
            command = "show City {}".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(o.__str__(), console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["Amenity.{}".format(o_id)]
            command = "show Amenity {}".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(o.__str__(), console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["Review.{}".format(o_id)]
            command = "show Review {}".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(o.__str__(), console.getvalue().strip())

    def test_show_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["BaseModel.{}".format(o_id)]
            command = "BaseModel.show({})".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(o.__str__(), console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["User.{}".format(o_id)]
            command = "User.show({})".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(o.__str__(), console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["State.{}".format(o_id)]
            command = "State.show({})".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(o.__str__(), console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["Place.{}".format(o_id)]
            command = "Place.show({})".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(o.__str__(), console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["City.{}".format(o_id)]
            command = "City.show({})".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(o.__str__(), console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["Amenity.{}".format(o_id)]
            command = "Amenity.show({})".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(o.__str__(), console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["Review.{}".format(o_id)]
            command = "Review.show({})".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(o.__str__(), console.getvalue().strip())


class TestHBNBCommand_destroy(unittest.TestCase):
    """Tests for destroy command of the HBNB console."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        storage.reload()

    def test_destroy_missing_class(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(".destroy()"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_destroy_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("MyModel.destroy()"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_destroy_id_missing_space_notation(self):
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy State"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy City"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy Place"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy Review"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_destroy_id_missing_dot_notation(self):
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy()"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("User.destroy()"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("State.destroy()"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("City.destroy()"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy()"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy()"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy()"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_destroy_invalid_id_space_notation(self):
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy User 1"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy State 1"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy City 1"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity 1"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy Place 1"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy Review 1"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_destroy_invalid_id_dot_notation(self):
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy(1)"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("User.destroy(1)"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("State.destroy(1)"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("City.destroy(1)"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy(1)"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy(1)"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy(1)"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_destroy_objects_space_notation(self):

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["BaseModel.{}".format(o_id)]
            command = "destroy BaseModel {}".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(o, storage.all())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["User.{}".format(o_id)]
            command = "show User {}".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(o, storage.all())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["State.{}".format(o_id)]
            command = "show State {}".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(o, storage.all())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["Place.{}".format(o_id)]
            command = "show Place {}".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(o, storage.all())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["City.{}".format(o_id)]
            command = "show City {}".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(o, storage.all())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["Amenity.{}".format(o_id)]
            command = "show Amenity {}".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(o, storage.all())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["Review.{}".format(o_id)]
            command = "show Review {}".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(o, storage.all())

    def test_destroy_objects_dot_notation(self):

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["BaseModel.{}".format(o_id)]
            command = "BaseModel.destroy({})".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(o, storage.all())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["User.{}".format(o_id)]
            command = "User.destroy({})".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(o, storage.all())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["State.{}".format(o_id)]
            command = "State.destroy({})".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(o, storage.all())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["Place.{}".format(o_id)]
            command = "Place.destroy({})".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(o, storage.all())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["City.{}".format(o_id)]
            command = "City.destroy({})".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(o, storage.all())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["Amenity.{}".format(o_id)]
            command = "Amenity.destroy({})".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(o, storage.all())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            o = storage.all()["Review.{}".format(o_id)]
            command = "Review.destory({})".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(o, storage.all())


class TestHBNBCommand_all(unittest.TestCase):
    """Tests for all command of the HBNB console."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_all_invalid_class(self):
        expected = "** class doesn't exist **"

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("MyModel.all()"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_all_objects_space_notation(self):

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("BaseModel", console.getvalue().strip())
            self.assertIn("User", console.getvalue().strip())
            self.assertIn("State", console.getvalue().strip())
            self.assertIn("Place", console.getvalue().strip())
            self.assertIn("City", console.getvalue().strip())
            self.assertIn("Amenity", console.getvalue().strip())
            self.assertIn("Review", console.getvalue().strip())

    def test_all_objects_dot_notation(self):

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(".all()"))
            self.assertIn("BaseModel", console.getvalue().strip())
            self.assertIn("User", console.getvalue().strip())
            self.assertIn("State", console.getvalue().strip())
            self.assertIn("Place", console.getvalue().strip())
            self.assertIn("City", console.getvalue().strip())
            self.assertIn("Amenity", console.getvalue().strip())
            self.assertIn("Review", console.getvalue().strip())

    def test_all_single_object_space_notation(self):

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertIn("BaseModel", console.getvalue().strip())
            self.assertNotIn("User", console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertIn("User", console.getvalue().strip())
            self.assertNotIn("BaseModel", console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            self.assertIn("State", console.getvalue().strip())
            self.assertNotIn("BaseModel", console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("all City"))
            self.assertIn("City", console.getvalue().strip())
            self.assertNotIn("BaseModel", console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
            self.assertIn("Amenity", console.getvalue().strip())
            self.assertNotIn("BaseModel", console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
            self.assertIn("Place", console.getvalue().strip())
            self.assertNotIn("BaseModel", console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
            self.assertIn("Review", console.getvalue().strip())
            self.assertNotIn("BaseModel", console.getvalue().strip())

    def test_all_single_object_dot_notation(self):

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", console.getvalue().strip())
            self.assertNotIn("User", console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", console.getvalue().strip())
            self.assertNotIn("BaseModel", console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn("State", console.getvalue().strip())
            self.assertNotIn("BaseModel", console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn("City", console.getvalue().strip())
            self.assertNotIn("BaseModel", console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertIn("Amenity", console.getvalue().strip())
            self.assertNotIn("BaseModel", console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertIn("Place", console.getvalue().strip())
            self.assertNotIn("BaseModel", console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertIn("Review", console.getvalue().strip())
            self.assertNotIn("BaseModel", console.getvalue().strip())


class TestHBNBCommand_update(unittest.TestCase):
    """Tests for update command of the HBNB console."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_update_missing_class(self):
        expected = "** class name missing **"

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(".update()"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_update_invalid_class(self):
        expected = "** class doesn't exist **"

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("MyModel.update()"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_update_missing_id_space_notation(self):
        expected = "** instance id missing **"

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update State"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update City"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update Amenity"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update Place"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update Review"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_update_missing_id_dot_notation(self):
        expected = "** instance id missing **"

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.update()"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("User.update()"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("State.update()"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("City.update()"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Amenity.update()"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Place.update()"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Review.update()"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_update_invalid_id_space_notation(self):
        expected = "** no instance found **"

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 1"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update User 1"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update State 1"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update City 1"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update Amenity 1"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update Place 1"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update Review 1"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_update_invalid_id_dot_notation(self):
        expected = "** no instance found **"

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.update(1)"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("User.update(1)"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("State.update(1)"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("City.update(1)"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Amenity.update(1)"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Place.update(1)"))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Review.update(1)"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_update_missing_attr_name_space_notation(self):
        expected = "** attribute name missing **"

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            o_id = console.getvalue().strip()
            testCmd = "update BaseModel {}".format(o_id)

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            o_id = console.getvalue().strip()
            testCmd = "update User {}".format(o_id)

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            o_id = console.getvalue().strip()
            testCmd = "update State {}".format(o_id)

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            o_id = console.getvalue().strip()
            testCmd = "update City {}".format(o_id)

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            o_id = console.getvalue().strip()
            testCmd = "update Amenity {}".format(o_id)

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            o_id = console.getvalue().strip()
            testCmd = "update Place {}".format(o_id)

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

    def test_update_missing_attr_name_dot_notation(self):
        expected = "** attribute name missing **"

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            o_id = console.getvalue().strip()
            testCmd = "BaseModel.update({})".format(o_id)

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            o_id = console.getvalue().strip()
            testCmd = "User.update({})".format(o_id)

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            o_id = console.getvalue().strip()
            testCmd = "State.update({})".format(o_id)

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            o_id = console.getvalue().strip()
            testCmd = "City.update({})".format(o_id)

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            o_id = console.getvalue().strip()
            testCmd = "Amenity.update({})".format(o_id)

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            o_id = console.getvalue().strip()
            testCmd = "Place.update({})".format(o_id)

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

    def test_update_missing_attr_value_space_notation(self):
        expected = "** value missing **"

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create BaseModel")
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            testCmd = "update BaseModel {} attr_name".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create User")
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            testCmd = "update User {} attr_name".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create State")
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            testCmd = "update State {} attr_name".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create City")
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            testCmd = "update City {} attr_name".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Amenity")
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            testCmd = "update Amenity {} attr_name".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Place")
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            testCmd = "update Place {} attr_name".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Review")
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            testCmd = "update Review {} attr_name".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

    def test_update_missing_attr_value_dot_notation(self):
        expected = "** value missing **"

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create BaseModel")
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            testCmd = "BaseModel.update({}, attr_name)".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create User")
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            testCmd = "User.update({}, attr_name)".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create State")
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            testCmd = "State.update({}, attr_name)".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create City")
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            testCmd = "City.update({}, attr_name)".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Amenity")
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            testCmd = "Amenity.update({}, attr_name)".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Place")
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            testCmd = "Place.update({}, attr_name)".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Review")
            o_id = console.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as console:
            testCmd = "Review.update({}, attr_name)".format(o_id)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, console.getvalue().strip())

    def test_update_valid_string_attr_space_notation(self):

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create BaseModel")
            o_id = console.getvalue().strip()
        testCmd = "update BaseModel {} attr_name 'attr_value'".format(o_id)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["BaseModel.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])


        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create User")
            o_id = console.getvalue().strip()
        testCmd = "update User {} attr_name 'attr_value'".format(o_id)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["User.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])


        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create State")
            o_id = console.getvalue().strip()
        testCmd = "update State {} attr_name 'attr_value'".format(o_id)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["State.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])


        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create City")
            o_id = console.getvalue().strip()
        testCmd = "update City {} attr_name 'attr_value'".format(o_id)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["City.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])


        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Place")
            o_id = console.getvalue().strip()
        testCmd = "update Place {} attr_name 'attr_value'".format(o_id)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])


        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Amenity")
            o_id = console.getvalue().strip()
        testCmd = "update Amenity {} attr_name 'attr_value'".format(o_id)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Amenity.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])


        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Review")
            o_id = console.getvalue().strip()
        testCmd = "update Review {} attr_name 'attr_value'".format(o_id)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Review.{}".format(o_id)].__dict__
        self.assertTrue("attr_value", test_dict["attr_name"])

    def test_update_valid_string_attr_dot_notation(self):

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create BaseModel")
            tId = console.getvalue().strip()
        testCmd = "BaseModel.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["BaseModel.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])


        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create User")
            tId = console.getvalue().strip()
        testCmd = "User.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["User.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])


        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create State")
            tId = console.getvalue().strip()
        testCmd = "State.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["State.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])


        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create City")
            tId = console.getvalue().strip()
        testCmd = "City.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["City.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])


        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Place")
            tId = console.getvalue().strip()
        testCmd = "Place.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])


        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Amenity")
            tId = console.getvalue().strip()
        testCmd = "Amenity.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Amenity.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])


        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Review")
            tId = console.getvalue().strip()
        testCmd = "Review.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Review.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_int_attr_space_notation(self):

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Place")
            o_id = console.getvalue().strip()
        testCmd = "update Place {} max_guest 98".format(o_id)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(o_id)].__dict__
        self.assertEqual("98", test_dict["max_guest"])

    def test_update_valid_int_attr_dot_notation(self):

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Place")
            tId = console.getvalue().strip()
        testCmd = "Place.update({}, max_guest, 98)".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(tId)].__dict__
        self.assertEqual("98", test_dict["max_guest"])

    def test_update_valid_float_attr_space_notation(self):

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Place")
            o_id = console.getvalue().strip()
        testCmd = "update Place {} latitude 7.2".format(o_id)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(o_id)].__dict__
        self.assertEqual('7.2', test_dict["latitude"])

    def test_update_valid_float_attr_dot_notation(self):

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Place")
            tId = console.getvalue().strip()
        testCmd = "Place.update({}, latitude, 7.2)".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(tId)].__dict__
        self.assertEqual('7.2', test_dict["latitude"])

    def test_update_valid_dictionary_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create BaseModel")
            o_id = console.getvalue().strip()
        testCmd = "update BaseModel {} ".format(o_id)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["BaseModel.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create User")
            o_id = console.getvalue().strip()
        testCmd = "update User {} ".format(o_id)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["User.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create State")
            o_id = console.getvalue().strip()
        testCmd = "update State {} ".format(o_id)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["State.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create City")
            o_id = console.getvalue().strip()
        testCmd = "update City {} ".format(o_id)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["City.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Place")
            o_id = console.getvalue().strip()
        testCmd = "update Place {} ".format(o_id)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Amenity")
            o_id = console.getvalue().strip()
        testCmd = "update Amenity {} ".format(o_id)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Amenity.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Review")
            o_id = console.getvalue().strip()
        testCmd = "update Review {} ".format(o_id)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Review.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_dictionary_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create BaseModel")
            o_id = console.getvalue().strip()
        testCmd = "BaseModel.update({}".format(o_id)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["BaseModel.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create User")
            o_id = console.getvalue().strip()
        testCmd = "User.update({}, ".format(o_id)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["User.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create State")
            o_id = console.getvalue().strip()
        testCmd = "State.update({}, ".format(o_id)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["State.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create City")
            o_id = console.getvalue().strip()
        testCmd = "City.update({}, ".format(o_id)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["City.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Place")
            o_id = console.getvalue().strip()
        testCmd = "Place.update({}, ".format(o_id)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Amenity")
            o_id = console.getvalue().strip()
        testCmd = "Amenity.update({}, ".format(o_id)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Amenity.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Review")
            o_id = console.getvalue().strip()
        testCmd = "Review.update({}, ".format(o_id)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Review.{}".format(o_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_dictionary_with_int_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Place")
            o_id = console.getvalue().strip()
        testCmd = "update Place {} ".format(o_id)
        testCmd += "{'max_guest': 98})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(o_id)].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_dictionary_with_int_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Place")
            o_id = console.getvalue().strip()
        testCmd = "Place.update({}, ".format(o_id)
        testCmd += "{'max_guest': 98})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(o_id)].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_dictionary_with_float_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Place")
            o_id = console.getvalue().strip()
        testCmd = "update Place {} ".format(o_id)
        testCmd += "{'latitude': 9.8})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(o_id)].__dict__
        self.assertEqual(9.8, test_dict["latitude"])

    def test_update_valid_dictionary_with_float_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("create Place")
            o_id = console.getvalue().strip()
        testCmd = "Place.update({}, ".format(o_id)
        testCmd += "{'latitude': 9.8})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(o_id)].__dict__
        self.assertEqual(9.8, test_dict["latitude"])


class TestHBNBCommand_count(unittest.TestCase):
    """Tests for count command of the HBNB console."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_count_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("MyModel.count()"))
            self.assertEqual("0", console.getvalue().strip())

    def test_count_object(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("1", console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create User"))

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("1", console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create State"))

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("1", console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Place"))

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("1", console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create City"))

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("1", console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("1", console.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Review"))

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("1", console.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
