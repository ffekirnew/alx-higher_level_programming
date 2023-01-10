#!/usr/bin/python3
"""Define function write_file"""


def to_json_string(my_obj):
    """Change an object to a JSON file."""
    import json
    return json.dumps(my_obj)
