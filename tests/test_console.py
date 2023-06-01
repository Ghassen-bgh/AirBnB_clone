#!/usr/bin/python3
"""Unittest cases for console"""

import unittest
import console
import pep8
import sys
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class Test_BaseModel(unittest.TestCase):
    """Class for testing the console."""
    def test_pep8_console(self):
        """ Test for PEP8 ok. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")

    def test_help(self):
        """ Test for help command. """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            cont_EOF = f.getvalue()
            HBNBCommand().onecmd("help quit")
            cont_quit = f.getvalue()
            HBNBCommand().onecmd("help all")
            cont_all = f.getvalue()
            HBNBCommand().onecmd("help create")
            cont_create = f.getvalue()
            HBNBCommand().onecmd("help destroy")
            cont_destroy = f.getvalue()
            HBNBCommand().onecmd("help help")
            cont_help = f.getvalue()
            HBNBCommand().onecmd("help show")
            cont_show = f.getvalue()
            HBNBCommand().onecmd("help update")
            cont_update = f.getvalue()
        self.assertNotEqual(cont_EOF, "*** No help on EOF\n")
        self.assertNotEqual(cont_quit, "*** No help on quit\n")
        self.assertNotEqual(cont_all, "*** No help on all\n")
        self.assertNotEqual(cont_create, "*** No help on create\n")
        self.assertNotEqual(cont_destroy, "*** No help on destroy\n")
        self.assertNotEqual(cont_help, "*** No help on help\n")
        self.assertNotEqual(cont_show, "*** No help on show\n")
        self.assertNotEqual(cont_update, "*** No help on update\n")

    def test_quit(self):
        """ Test for quit command. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))
        self.assertEqual(f.getvalue(), "")
    
    def test_EOF(self):
        """ Test for EOF command. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))
        self.assertEqual(f.getvalue(), "")
    
    def test_emptyline(self):
        """ Test for emptyline command. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
        self.assertEqual(f.getvalue(), "")
    
    def test_create(self):
        """ Test for create command. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
        self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        self.assertEqual(len(f.getvalue()), 37)
    
    def test_show(self):
        """ Test for show command. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show"))
        self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
        self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 1234"))
        self.assertEqual(f.getvalue(), "** no instance found **\n")
    
    def test_destroy(self):
        """ Test for destroy command. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
        self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
        self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1234"))
        self.assertEqual(f.getvalue(), "** no instance found **\n")
    
    def test_all(self):
        """ Test for all command. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
        self.assertEqual(len(f.getvalue()), 2)

    def test_update(self):
        """ Test for update command. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
        self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 1234"))
        self.assertEqual(f.getvalue(), "** no instance found **\n")
