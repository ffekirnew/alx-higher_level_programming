#!/usr/bin/python3
"""Contain the function declaration for is_same_class."""


def is_same_class(obj, a_class):
    """Return True if obj is an instance of a_class, otherwise False."""
    return type(obj) == a_class
