#!/usr/bin/python3
"""User module that inherits from BaseModule"""
from models.base_model import BaseModel


class User(BaseModel):
    """user class that defines the user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
