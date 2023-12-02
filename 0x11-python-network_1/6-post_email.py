#!/usr/bin/python3
""" script that send a POST request with an email param,
then displays the body of the response decoded in utf-8. """
import requests
import sys

if __name__ == "__main__":
    payload = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], params=payload)
    print(r.text)
