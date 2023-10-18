#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

class BaseModel:
     def __init__(self, *args, **kwargs):
         from models import storage
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.save()
            storage.new(self)
        else:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def save(self):
        '''
        Update public instance with current datetime
        '''
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        '''
        String reprsentation
        '''
        return '[{}] ({}) {}'.format(
            type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        '''
        Dictionary containing all
        keys/values of __dict__
        '''
        my_dict = dict(self.__dict__)
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = type(self).__name__
        return my_dict
