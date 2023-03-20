import json


class FileStorage:
    """A class for serializing and deserializing instances
    to and from a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump({k: v.to_dict()
                      for k, v in self.__objects.items()}, file)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        # import other necessary models here
        classes = {"BaseModel": BaseModel, "User": User, "Place":  Place,
                   "State": State, "City": City, "Amenity": Amenity,
                   "Review": Review}
        # add other necessary models to the classes dictionary
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for obj_id, obj_attrs in obj_dict.items():
                    obj_cls = obj_attrs['__class__']
                    obj_attrs.pop('__class__', None)
                    obj_attrs.pop('__module__', None)
                    obj = classes[obj_cls](**obj_attrs)
                    self.all()[obj_id] = obj
        except FileNotFoundError:
            pass
