#!/usr/bin/python3
import os
sys.path.append('../../../AirBnB_clone')
import json
from model.base_model import BaseModel
class FileStorage:
    """A class for serializing and deserializing instances to and from a JSON file"""
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Return the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj
        
    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)"""
        objs_dict = {}
        for key, obj in self.__objects.items():
            objs_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(objs_dict, f)
            
    def reload(self):
        """Deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                objs_dict = json.load(f)
                for key, obj_dict in objs_dict.items():
                    cls_name, obj_id = key.split(".")
                    cls = globals()[cls_name]
                    obj = cls(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

