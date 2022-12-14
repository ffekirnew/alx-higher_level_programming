#!/usr/bin/python3
for decimal in range(100):
    print("{}{}".format(0 if (decimal < 10) else '', decimal), end="")
    print("".format(), end=", " if (decimal < 99) else "\n")
