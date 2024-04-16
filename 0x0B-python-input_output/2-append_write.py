#!/usr/bin/python3
""" Defines a Function to append text to specific file"""


def append_write(filename="", text=""):
    """append a UTF-8 string to a file.

    Args:
        filename (str): the name of a file to append text to
        text (str): the text to append to the file
    Returns:
        the number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
