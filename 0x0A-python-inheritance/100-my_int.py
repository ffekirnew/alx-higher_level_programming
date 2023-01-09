#!/usr/bin/python3
"""Define a class MyInt that inherits from int."""


class MyInt(int):
    """Define a rebel int."""

    def __eq__(self, __x):
        """Define a rebel equality."""
        return not super().__eq__(__x)

    def __ne__(self, __x):
        """Define a rebel inequality."""
        return super().__eq__(__x)
