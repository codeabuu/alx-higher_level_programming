#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":

    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
