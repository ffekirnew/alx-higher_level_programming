#!/usr/bin/python3
import sys

if __name__ == "__main__":
    summation = 0
    arguments = sys.argv
    for idx in range(1, len(arguments)):
        num = int(arguments[idx])
        summation += num
    print(summation)
