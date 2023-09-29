#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request


request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    print(dict(response.headers).get("X-Request-Id"))
