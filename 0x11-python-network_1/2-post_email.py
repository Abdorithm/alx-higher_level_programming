#!/usr/bin/python3
""" script that send a POST request with an email param,
then displays the body of the response decoded in utf-8. """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    payload = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    req = urllib.request.Request(url, payload)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
