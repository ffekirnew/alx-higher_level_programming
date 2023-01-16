#!/usr/bin/python3
"""Define function save_to_json_file."""


def save_to_json_file(my_obj, filename):
    """Write an Object to a text file, using a JSON representation."""
    import json
    with open(filename, 'w') as myfile:
        json.dump(my_obj, myfile)
