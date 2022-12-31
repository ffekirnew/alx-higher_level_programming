#!/usr/bin/python3
"""Module prints the name of a person.

contains functions: text_indentation
"""


def text_indentation(text):
    """Print text with 2 new lines after each of these characters: ., ? and :.

    Parameters
    ----------
    text : str
        The text to be printed

    Returns
    -------
    None

    Raises
    ------
    TypeError
        text is not a string

    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    idx = 0
    while idx < len(text):
        char = text[idx]
        print(char, end='')
        if char == '.' or char == '?' or char == ':':
            print('\n')
            idx += 1
        idx += 1
    print()
