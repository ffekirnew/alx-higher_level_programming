#!/usr/bin/python3


def best_score(a_dictionary):
    maximum = [None, None]
    for key, value in a_dictionary.items():
        if not maximum[0] or value > maximum[1]:
            maximum = [key, value]
    return maximum[0]
