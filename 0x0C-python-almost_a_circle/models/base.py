#!/usr/bin/python3
"""
Module to define Base
"""
import json
import csv


class Base:
    """
    Base of all other classes, managing id
    attribute to avoid duplicates.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
