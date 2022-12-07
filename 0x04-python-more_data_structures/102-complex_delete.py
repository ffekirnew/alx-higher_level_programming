#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return None
    new_dictionary = a_dictionary
    for key, key_value in new_dictionary.items():
        if key_value == value:
            del new_dictionary[key]
    return new_dictionary
