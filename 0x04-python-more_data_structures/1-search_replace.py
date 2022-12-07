#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i, element in enumerate(my_list):
        if search == element:
            new_list[i] = replace

    return new_list
