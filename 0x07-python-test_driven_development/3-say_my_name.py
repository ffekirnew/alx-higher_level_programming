#!/usr/bin/python3
"""Module prints the name of a person.

contains functions: say_my_name
"""


def say_my_name(first_name, last_name=""):
    """Print My name is <first name> <last name>.

    Parameters
    ----------
    first_name : str
        First Name
    last_name : str
        Last Name

    Returns
    -------
    None

    Raises
    ------
    TypeError
        If either first_name or last_name is not a string

    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print(f"My name is {first_name} {last_name}")
