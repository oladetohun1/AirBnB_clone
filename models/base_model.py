#!/usr/bin/python3
import uuid
import datetime


class BaseModel:
    """A base class for defining common attributes
    and methods for other classes"""

    def __init__(self):
        """Initialize a new instance of the BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Return a string representation of the BaseModel instance"""
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute updated_at with the
        current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance"""
        result = dict(self.__dict__)
        result['_class'] = type(self).__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()

        return result
