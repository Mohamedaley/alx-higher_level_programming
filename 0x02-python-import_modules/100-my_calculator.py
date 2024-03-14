#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1
    from sys import argv
    length == len(argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == '+':
        print("{} + {} = {}".format(argv[1], argv[3], a + b))
    elif argv[2] == '-':
        print("{} - {} = {}".format(argv[1], argv[3], a - b))
    elif argv[2] == '*':
        print("{} * {} = {}".format(argv[1], argv[3], a * b))
    elif argv[2] == '/':
        print("{} / {} = {}".format(argv[1], argv[3], a / b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
