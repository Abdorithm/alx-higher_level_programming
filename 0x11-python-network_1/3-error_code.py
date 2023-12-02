#!/usr/bin/python3
"""script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8). """
import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
        print(html.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
