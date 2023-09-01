#!/usr/bin/python3
"""
Reads json requests from server
"""
import requests
import sys
from sys import argv


if __name__ == "__main__":
    try:
        letter = sys.argv[1]
    except:
        letter = ""
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data={"q": letter}).json()
    if r == {}:
        print("No result")
    else:
        print("[{}] {}".format(r['id'], r['name']))
