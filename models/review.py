#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """class inheriting from BaseModel"""
    def __init__(self):
        """initialiazes class Review"""
        self.place_id = ""
        self.user_id = ""
        self.text = ""
