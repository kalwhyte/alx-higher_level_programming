#!/usr/bin/python3

"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request


def fetch_url(url):
    """
    Fetches the contents of the given URL.

    Args:
        url: A string representing the URL to fetch.

    Returns:
        The body of the HTTP response.
    """
    with urllib.request.urlopen(url) as response:
        return response.read()


def display_info(response):
    """
    Displays information about the HTTP response.

    Args:
        response: A bytes object representing the body of the HTTP response.
    """
    body = response.decode("utf-8")
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
    print("\t- utf8 content: {}".format(body))


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response_body = fetch_url(url)
    display_info(response_body)
