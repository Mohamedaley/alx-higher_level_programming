#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    else:
        new = number % 10
    print("{}".format(new), end="")
    return (new)