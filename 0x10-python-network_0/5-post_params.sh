#!/bin/bash
# Takes a URL and sends a POST request to the URL passed
curl "$1" -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
