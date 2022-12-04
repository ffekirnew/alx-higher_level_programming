#!/usr/bin/python3


def max_integer(my_list=[]):
    if not my_list:
        return None
    maximum = my_list[0]
    for elem in my_list:
        maximum = elem if elem > maximum else maximum
    return maximum
