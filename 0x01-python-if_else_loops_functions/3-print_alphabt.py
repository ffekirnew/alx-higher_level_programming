#!/usr/bin/python3
for ascii_index in range(97, 123):
    if (ascii_index == 101 or ascii_index == 113):
        continue
    print("{}".format(chr(ascii_index)), end="")
