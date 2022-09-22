#!/bin/bash
# a Bash script that sends a request to a URL passed as an argument, and display#s only the status code of the response.
curl -s -X POST -H "Content-Type: application/json" "$1" -d @"$2"
