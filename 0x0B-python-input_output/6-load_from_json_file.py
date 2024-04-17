#!/usr/bin/python3
""" Defines a function to creat an object from JSON file"""
import json


def load_from_json_file(filename):
    """ creating an object from Json file"""
    with open(filename, 'r') as file:
        return json.load(file)
