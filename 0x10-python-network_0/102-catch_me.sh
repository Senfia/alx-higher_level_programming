#!/bin/bash
# makes a request to a URL that causes the server to respose with a specific message
curl -sL -X 0.0.0.0:5000/catch_me PUT -H "user_id=98" -d "Origin: You got me!"
