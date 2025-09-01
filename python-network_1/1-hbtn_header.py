#!/usr/bin/python3
"""Fetches the X-Request-Id header value from a given URL."""
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.info()
    print(headers.get('X-Request-Id'))
