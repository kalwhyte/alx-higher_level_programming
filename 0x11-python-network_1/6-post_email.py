#!/usr/bin/env python3
"""
Sends a POST request to a URL with an email as a parameter.

Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    payload = {"email": sys.argv[2]}

    r = requests.post(url, data=payload)
    print(r.text)
