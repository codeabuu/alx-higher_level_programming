#!/bin/bash
# send a request to an URL with curl, and displays the size of the body of the response
curl -sI "$1" | grep -i 'content-length' | awk '{print $2}' | tr -d '\r'
