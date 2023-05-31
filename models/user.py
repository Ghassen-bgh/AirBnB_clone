#!/usr/bin/python3
"""
Module for User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User class
    """
    def __init__(self, *args, **kwargs):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(*args, **kwargs)

    def __str__(self):
        return "[{}] ({}) {} {}".format(
            self.__class__.__name__, self.id, self.email, self.__dict__)

