#!/usr/bin/python3
"""Contain class definition for MyList."""


class MyList(list):
    """Add other functionalities to builtin list."""

    def print_sorted(self):
        """Print sorted list (ascending sort)."""
        sorted_list = sorted(self)

        print(sorted_list)
