#!/bin/bash
#a Bash script that takes in a URL, sends a request to that URL
echo "$(curl -s -w '%{size_download}' -o /dev/null $1)"
