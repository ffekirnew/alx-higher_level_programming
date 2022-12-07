#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    elements = 0
    for my_tuple in my_list:
        total += my_tuple[0] * my_tuple[1]
        elements += my_tuple[1]
    return total / elements
