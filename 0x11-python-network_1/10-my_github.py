#!/usr/bin/python3
""" takes GitHub credentials (username and password) and uses
the GitHub API to display your id """
import sys
import requests


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/users/{}'.format(username)

    headers = {
            'Authorization': password,
            'Accept': 'application/vnd.github.v3+json'
    }
    r = requests.get(url, headers=headers)
    print(r.json().get('id'))
