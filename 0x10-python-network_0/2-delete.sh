#!/bin/bash
# a Bash script that sends a DELETE request to the URL passed as the first argum#ent and displays the body of the response
curl -sLX DELETE "$1"
