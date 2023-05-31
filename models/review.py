#!/usr/bin/python3
""" Module for Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class definition """
    def __init__(self, *args, **kwargs):
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(*args, **kwargs)

    def __str__(self):
        return "[{}] ({}) {} - {}".format(
            self.__class__.__name__, self.id, self.text, self.place_id)
