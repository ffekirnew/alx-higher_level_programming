#!/usr/bin/python3
"""Define function write_file"""


def append_write(filename="", text=""):
    """Appends the text into the file given and print the contents."""
    with open(filename, 'a', encoding='utf8') as file:
        number_characters_added = file.write(text)
    return number_characters_added
