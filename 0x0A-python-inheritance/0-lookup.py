#!/usr/bin/python3
"""Module contains the function lookup."""


def lookup(obj):
    """Return a list containing attributes and methods of an object.
    Parameters:
        obj - any object.

    Return:
        list of attributes and methods available to it.
    """
    attributes_and_methods = []

    for element in dir(obj):
        attributes_and_methods.append(element)

    return attributes_and_methods
