#!/usr/bin/python3
import json
"""
from_json_string module.
It contains one function.
"""


def from_json_string(my_str):
    """
    Return an object represented by a JSON string.
    """
    return json.loads(my_str)
