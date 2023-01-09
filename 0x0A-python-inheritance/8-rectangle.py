#!/usr/bin/python3
"""Define a class that represents rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define a rectangle class."""

    def __init__(self, width, height):
        """Construct a rectangle with width and height.
        Parameters:
            width: the width of the rectangle.
            height: the height of the rectangle.
        """
        super().__init__()
        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)
