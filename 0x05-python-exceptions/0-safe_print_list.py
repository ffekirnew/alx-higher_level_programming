#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    while True:
        try:
            print(my_list[count], end='')
            count += 1
        except IndexError:
            print()
            break
    return count
