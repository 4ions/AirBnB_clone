#!/usr/bin/python3
""" Module of Base class """
import uuid
from datetime import datetime


class BaseModel:
    """ Class Base Model """
    
    def __init__(self):
        """ Init """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):
        """ Dictionary containing all key/values """
        dictionary = {}
        for key, item in self.__dict__.items():
            if key in ['updated_at', 'created_at']:
                dictionary[key] = item.isoformat()
            else:
                dictionary[key] = item
        dictionary['__class__'] = self.__class__.__name__
        return dictionary

