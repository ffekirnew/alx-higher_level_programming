#!/usr/bin/python3
"""This module contains a function that adds two integers

The function will take in inputs a, and b (optional) and will
return the sum.
"""


def add_integer(a, b=98):
    '''Adds two integers
    returns: a + b
    '''
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    a, b = int(a), int(b)
    return a + b
