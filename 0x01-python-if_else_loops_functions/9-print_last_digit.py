#!/usr/bin/python3


def print_last_digit(number):
    number *= 1 if (number > 0) else -1
    print(f"{number % 10}", end="")
    return (number % 10)
