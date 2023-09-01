#!/usr/bin/python3
"""
Handles a http status code >= 400 (error) with requests
"""
import requests
import sys
from sys import argv


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
