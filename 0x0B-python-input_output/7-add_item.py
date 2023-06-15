#!/usr/bin/python3
"""
load_from_json_file module.
It contains one function.
"""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
try:
    arg = load_from_json_file("add_item.json")
except:
    arg = []
for itm in range(1, len(sys.argv)):
    arg.append(sys.argv[itm])
save_to_json_file(arg, "add_item.json")
