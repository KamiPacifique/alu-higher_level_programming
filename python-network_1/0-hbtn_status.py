#!/usr/bin/python3
"""Fetch a URL and display the response body info using urllib."""
import urllib.request

url = "http://0.0.0.0:5050/status"

with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode("utf-8"))
