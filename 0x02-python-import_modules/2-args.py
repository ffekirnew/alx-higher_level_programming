#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    no_of_arguments = len(argv) - 1
    if not no_of_arguments:
        print("0 arguments.")
    elif no_of_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(no_of_arguments))
    for i, arg in enumerate(argv):
        if not i:
            continue
        print("{}: {}".format(i, arg))
