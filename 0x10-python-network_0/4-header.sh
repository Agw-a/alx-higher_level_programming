#!/bin/bash
# a Bash script that takes in a URL as an argument, sends a GET request to the U#RL, and displays the body of the response
curl -sLX GET "$1" -H "X-School-User-Id: 98"
