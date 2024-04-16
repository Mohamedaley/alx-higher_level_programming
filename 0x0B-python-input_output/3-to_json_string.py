#!/usr/bin/python3
"""Defines a function to return JSON repre of an obj"""
import json


def to_json_string(my_obj):
    """Returns the json repre of an obj"""
    return json.dumps(my_obj)
