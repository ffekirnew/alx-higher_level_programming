#!/usr/bin/python3
"""Define a class that represents rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a square class that inherits from a rectangle class."""

    def __init__(self, size):
        """Construct a rectangle with width and height.
        Parameters:
            width: the width of the rectangle.
            height: the height of the rectangle.
        """
        try:
            self.integer_validator('size', size)
            self.__size = size
            super().__init__(size, size)
        except ValueError as e:
            raise e
        except TypeError as e:
            raise e
