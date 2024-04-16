#!/usr/bin/python3
"""Defines a text file-writing function."""


def write_file(filename="", text=""):
    with open(filename, encoding="utf-8") as file:
        return file.write(text)
