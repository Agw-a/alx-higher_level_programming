#!/bin/bash
#a Bash script that takes in a URL, sends a request to that URL, and displays th#e size of the body of the response
curl -s -I "$1" | grep "Content-Length" | cut -d " " -f 2
