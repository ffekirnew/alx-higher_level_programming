#!/usr/bin/python3
import sys

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if not i:
            continue
        print("{}: {}".format(i, arg))
