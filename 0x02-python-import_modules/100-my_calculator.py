#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argv = list(argv)
    operators = ['+', '-', '*', '/']
    ops = [add, sub, mul, div]
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a, b, op = int(argv[1]), int(argv[3]), argv[2]
    print("{} {} {} = {}".format(a, op, b, ops[operators.index(op)](a, b)))
