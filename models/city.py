#!/usr/bin/python3
""" Module for City class """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class definition """
    def __init__(self, *args, **kwargs):
        self.state_id = ""
        self.name = ""
        super().__init__(*args, **kwargs)

    def __str__(self):
        return "[{}] ({}) {} - {}".format(
            self.__class__.__name__, self.id, self.name, self.state_id)
