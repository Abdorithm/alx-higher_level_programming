#!/usr/bin/python3
"""defines the from_json_string method"""
import json


def from_json_string(my_obj):
    """return an object (Python data structure) represented by a JSON string"""
    data = json.loads(my_obj)
    return data
