#!/bin/bash
# makes a request to a URL that causes the server to respose with a specific message
curl -Ls -H "Origin: You got me!" -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
