#!/usr/bin/python3
""" Module of user """

from models.base_model import BaseModel


class User(BaseModel):
    """ Class of user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
