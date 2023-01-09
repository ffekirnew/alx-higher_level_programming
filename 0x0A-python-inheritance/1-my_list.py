#!/usr/bin/python3
"""Contain class definition for MyList."""


class MyList(list):
    """Add other functionalities to builtin list."""

    def __init__(self, *arg):
        """Construct an instance of the class."""
        list.__init__(self, *arg)

    def print_sorted(self):
        """Print sorted list (ascending sort)."""
        sorted_list = sorted(self)

        print(sorted_list)
