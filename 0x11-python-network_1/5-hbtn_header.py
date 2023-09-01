#!/usr/bin/python3
"""
Uses requests module yo get header info.
"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
