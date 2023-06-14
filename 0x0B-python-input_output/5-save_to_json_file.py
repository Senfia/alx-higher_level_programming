#!/usr/bin/python3
"""
save_to_json_file module.
It contains one function.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    returns an object (Python data structure)
    represented by a JSON string
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
