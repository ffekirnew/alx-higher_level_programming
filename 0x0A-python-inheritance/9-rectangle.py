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

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self) -> str:
        """Style representation of the class."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
