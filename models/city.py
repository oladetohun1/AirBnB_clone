#!/usr/bin/python3
"""City class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that contains state id and  state name"""
    state_id = ""
    name = ""
