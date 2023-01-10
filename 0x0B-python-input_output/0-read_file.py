#!/usr/bin/python3
"""Define function read_file"""


def read_file(filename=""):
    """Read the file and print the contents."""
    with open(filename, mode='r', encoding='UTF8') as file:
        print(file.read())
