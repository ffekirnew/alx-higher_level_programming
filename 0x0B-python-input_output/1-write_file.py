#!/usr/bin/python3
"""Define function write_file"""


def write_file(filename="", text=""):
    """Write the text into the file and print the contents."""
    with open(filename, mode='w', encoding='UTF8') as file:
        data = file.write(text)
