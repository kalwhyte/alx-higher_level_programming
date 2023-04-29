#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import requests


if _name_ == "_main_":
    reqt = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(reqt.text)))
    print("\t- content: {}".format(reqt.text))
