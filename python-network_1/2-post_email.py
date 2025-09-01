#!/usr/bin/python3
"""Sends a POST request to a given URL with an email parameter and displays the response."""
import urllib.parse
import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]

# Encode the email into a dictionary, then into bytes
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

# Perform the POST request and read the response
with urllib.request.urlopen(url, data=data) as response:
    print(response.read().decode('utf-8'))
