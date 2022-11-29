#!/usr/bin/python3
for decimal in range(100):
    print(f"{0 if (decimal < 10) else ''}{decimal}", end="")
    print("", end=", " if (decimal < 99) else "\n")
