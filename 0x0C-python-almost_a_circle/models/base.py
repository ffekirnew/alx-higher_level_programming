#!/usr/bin/python3
"""Contains class definition for the class Base."""


class Base:
    """Define the class base.

    Class Attribues:
    ----------------
    __nb_objects - keeps track of the number of object of the class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance of the class Base."""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
