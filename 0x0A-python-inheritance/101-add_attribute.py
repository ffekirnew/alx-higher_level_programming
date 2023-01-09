#!/usr/bin/python3
"""Define function add_attribute."""


def add_attribute(_class, new_attr, new_value):
    """Add attribute to the _class."""
    if not hasattr(_class, new_attr):
        setattr(_class, new_attr, new_value)
    else:
        raise TypeError("can't add new attribute")
