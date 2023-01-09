#!/usr/bin/python3
"""Contain empty class definition for BaseGeometry."""


class BaseGeometry:
    """Define the class BaseGeometry."""

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise TypeError(f"{name} must be greater than 0")
