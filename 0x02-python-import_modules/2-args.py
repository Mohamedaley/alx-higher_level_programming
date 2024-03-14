#!/usr/bin/python3
from sys import argv

length = len(argv)
for item in range(1, length):
    print("{}: {}".format(item, argv[item]))
