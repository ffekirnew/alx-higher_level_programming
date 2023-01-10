#!/usr/bin/python3
"""Define function load_from_json_file"""


def load_from_json_file(filename):
    """Load from a json file and return the file."""
    import json
    with open(filename, 'r') as myfile:
        return json.load(myfile)
