#!/usr/bin/python3
"""Module prints the name of a person.

contains functions: print_square
"""


def print_square(size):
    """Print a square of size size.

    Parameters
    ----------
    size : int
        The size length of the square

    Returns
    -------
    None

    Raises
    ------
    TypeError
        If size is not an integer
    ValueError
        If size is less than zero

    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
