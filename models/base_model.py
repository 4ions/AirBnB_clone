#!/usr/bin/python3
""" Module of Base class """
import uuid
from datetime import datetime


class BaseModel:
    """ Class Base Model """
    
    def __init__(self):
        """ Init """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.update_at = datetime.now().isoformat()

    def __str__(self):
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):
        """ Dictionary containing all key/values """
        
        dictionary = {
                    "my_number": self.my_number,
                    "name": self.name,
                    "__class__": type(self),
                    "updated_at": self.update_at,
                    "id": self.id,
                    "created_at": self.created_at
                    }
        return dictionary

