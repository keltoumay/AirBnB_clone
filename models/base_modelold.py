#!/usr/bin/python3
"""
Write a class that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    A class that defines all common attributes/methods for other classes
    """
    def __init__(self):
        """
        Initializes the attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        string representaition of something
        """
        return (
            "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
            )
        )

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        """
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
