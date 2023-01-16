#!/usr/bin/python3
"""Define function write_file"""


def write_file(filename="", text=""):
    """Write the text into the file and print the contents."""
    with open(filename, mode='w', encoding='utf8') as file:
        number_characters_written = file.write(text)

    return number_characters_written
