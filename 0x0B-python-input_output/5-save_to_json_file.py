#!/usr/bin/python3
""" Defines a function to save object in a file"""
import json


def save_to_json_file(my_obj, filename):
    """Function to save a python object in a json format file"""
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
