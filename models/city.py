#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """defines a class city"""
    def __init__(self):
        """initializes class city"""
        self.state_id = ""
        self.name = ""
