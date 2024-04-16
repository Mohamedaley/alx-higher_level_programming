#!/usr/bin/python3
"""Defines a Function to write into a text file"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file which i will write in.
        text (str): The text to be written into the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
