#!/usr/bin/python3
"""Defines a func to serialize and object and return int"""
import json


def from_json_string(my_str):
    """ Serializing an object and returns it (JSON Representation)"""
    return json.loads(my_str)