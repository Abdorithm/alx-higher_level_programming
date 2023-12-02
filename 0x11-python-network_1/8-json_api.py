#!/usr/bin/python3
""" sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter. """
import sys
import requests

if __main__ == "__name__":
    if len(sys.argv) != 1:
        p = ""
    else:
        p = sys.argv[1]
    payload = {"p": p}

    r = requests.get('http://0.0.0.0:5000/search_user', params=payload)

    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
