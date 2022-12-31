#!/usr/bin/python3
"""This module contains a function that adds two integers."""


def add_integer(a, b=98):
    """Add two integers.
    
    Parameters
    ----------
    a : any
        The first operand
    b : any
        The Second Operand

    Returns
    -------
    int
        the sum of the two arguments
    
    Raises
    ------
    TypeError
        If either a or b are not numbers

    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    a, b = int(a), int(b)
    return a + b
