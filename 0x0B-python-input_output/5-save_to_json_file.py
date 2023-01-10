#!/usr/bin/python3
"""Define function write_file"""


def from_json_string(my_str):
    """Change an object to a JSON file."""
    import json
    return json.loads(my_str)
