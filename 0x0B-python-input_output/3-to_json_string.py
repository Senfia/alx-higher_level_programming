#!/usr/bin/python3
"""
to_json_string module.
It contains one function.
"""
import json


def to_json_string(my_obj):
    """
    Return the JSON of an object
    """
    return json.dumps(my_obj)
