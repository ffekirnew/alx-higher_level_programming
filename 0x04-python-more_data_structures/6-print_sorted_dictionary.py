#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    a_list = [[key, value] for key, value in a_dictionary.items()]
    a_list.sort(key=lambda x: ord(x[0][0]))
    for item in a_list:
        print(item[0] + ": ", item[1])
