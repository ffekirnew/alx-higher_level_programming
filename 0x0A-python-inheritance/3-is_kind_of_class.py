#!/usr/bin/python3
"""Contain the definition for function is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of, or
    if the object is an instance of a class that inherited from,
    the specified class.
    """

    return isinstance(obj, a_class)
