#!/usr/bin/python3
def uppercase(str):
    while (str[i]):
        if ord(str[i]) >= 65 and ord(str[i]) <= 90:
            new = str[i]
        else:
            new = ord(str[i]) + 32
        print("{}".format(new), end="")
