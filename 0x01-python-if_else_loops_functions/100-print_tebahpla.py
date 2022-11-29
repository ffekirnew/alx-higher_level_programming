#!/usr/bin/python3
case = False # True for upper, False for lower
for i in range(122,96,-1):
    print(f"{chr(i - 32) if (case) else chr(i)}", end="")
    case = not case
