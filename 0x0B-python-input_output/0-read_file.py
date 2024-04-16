#!/usr/bin/python3
def read_file(filename=""):
    with (open(filename, 'w')) as file:
        data = file.read()
    print(data)
