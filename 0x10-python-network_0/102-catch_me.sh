#!/bin/bash
# makes a request to a URL that causes the server to respose with a specific message
curl -s 0.0.0.0:5000/catch_me -X PUT -L -d "user_id=98" -H "Origin: You got me!"
