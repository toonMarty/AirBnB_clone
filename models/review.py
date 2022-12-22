#!/usr/bin/python3
""" Review module that defines a Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ This review class defines a review """
    place_id = ""
    user_id = ""
    text = ""
