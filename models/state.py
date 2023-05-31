#!/usr/bin/python3
"""Module for class State
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class State
    """
    def __init__(self, *args, **kwargs):
        self.name = ""
        super().__init__(*args, **kwargs)

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.name)
