#!/usr/bin/python3
"""
Module for Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class model """
    def __init__(self, *args, **kwargs):
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        super().__init__(*args, **kwargs)

    def __str__(self):
        return "[{}] ({}) {} - {}".format(
            self.__class__.__name__, self.id, self.name, self.city_id)
