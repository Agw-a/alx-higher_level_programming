#!/bin/bash
# a Bash script that takes in a URL, sends a GET request to the URL, and display#s the body of the response
curl -sLX GET "$1"
