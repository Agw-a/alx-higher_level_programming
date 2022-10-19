#!/bin/bash
#a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the ser#ver to respond with a message containing You got me!, in the body of response
curl -sLX PUT 0.0.0.0:5000/catch_me -H "You got me!"
