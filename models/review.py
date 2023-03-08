#!/usr/bin/python3
"""Review module that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class to store review information"""
    place_id = ""
    usr_id = ""
    text = ""
