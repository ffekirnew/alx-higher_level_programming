#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    answer = [not elem % 2 for elem in my_list]
    return answer
