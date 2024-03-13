#!/usr/bin/python3

for index in range(0, 10):
    for index1 in range(index + 1, 10):
        if index == 8 and index1 == 9:
            print("{}{}".format(index, index1))
        else:
            print("{}{}, ".format(index, index1), end="")
