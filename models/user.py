#!/usr/bin/python3
#from models.base_model import BaseModel


#class User(BaseModel):
#    """class that inherits from BaseModel"""
#    def __init__(self):
#        """initializes class user"""
#        super().__init__()
#       self.email = ""
#       self.password = ""
#       self.first_name = ""
#       self.last_name = ""
from models.base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialization of User instance"""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")


