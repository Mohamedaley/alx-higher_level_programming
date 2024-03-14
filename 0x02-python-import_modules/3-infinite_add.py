#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    total = 0
    length = len(argv) - 1
    for item in range(length):
        total = total + int(argv[item + 1])
print("{}".format(total))
