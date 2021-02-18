#!/usr/bin/python3
""" Module of city """

from models.base_model import BaseModel


class City(BaseModel):
    """ Base class for city models """
    state_id = ""
    name = ""
