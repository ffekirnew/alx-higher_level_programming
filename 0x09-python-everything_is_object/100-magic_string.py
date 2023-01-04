#!/usr/bin/python3
def magic_string():
    for i in range(11):
        for j in range(i): print("BestSchool", end=', ' if j < i - 1 else '\n')
