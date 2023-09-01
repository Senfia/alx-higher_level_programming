#!/usr/bin/python3
"""
makes a Post request using requests
"""

import requests
import sys
from sys import argv

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    param = {'email': email}
    r = requests.post(url, data=param)
    print(r.text)
