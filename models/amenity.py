#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """defines a class amenity"""
    def __init__(self):
        """initilaizes amenity class"""
        self.name = ""
