#!/usr/bin/python3
import uuid
from datetime import datetime
from models.__init__ import storage

class BaseModel:
    """A base class for defining common attributes
    and methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at','updated_at'):
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
                elif key != '__class__':
                    setattr(self, key, value)
            self.id = kwargs.get('id', str(uuid.uuid4()))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute updated_at with the
        current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance"""
        result_copy = self.__dict__.copy()
        result_copy['__class__'] = self.__class__.__name__
        result_copy['created_at'] = self.created_at.isoformat()
        result_copy['updated_at'] = self.updated_at.isoformat()
        return result_copy

