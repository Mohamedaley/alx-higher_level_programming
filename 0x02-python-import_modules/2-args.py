#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    length = len(argv) - 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
    else:
        print("{} arguments".format(length))
    for item in range(length):
        print("{}: {}".format(item + 1, argv[item + 1]))
