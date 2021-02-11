#!/usr/bin/python3
""" Module of Base class """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ Class Base Model """
    
    def __init__(self, *args, **kwargs):
        """ Init """
        if kwargs:
            for key, item in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    item = datetime.strptime(str(item), "%Y-%m-%dT%H:%M:%S.%f")
                if key not in ['__class__']:
                    setattr(self, key, item)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

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

