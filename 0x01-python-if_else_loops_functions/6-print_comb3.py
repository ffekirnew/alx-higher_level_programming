#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (i < j):
            print(f"{i}{j}", end="")
            print("", end="\n" if (i == 8 and j == 9) else ", ")