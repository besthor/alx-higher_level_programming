#!/bin/bash
# A Bash script that takes in a URL, sends a GET request and displays only the  body of a 200 status code response
curl -Ls "$1"
