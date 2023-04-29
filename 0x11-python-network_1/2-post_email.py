#!/usr/bin/python3
"""sends a POST request to the passed URL with the given email.

Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode("ascii")

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
