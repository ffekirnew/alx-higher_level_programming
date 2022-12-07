#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return None
    new_dictionary = a_dictionary
    to_be_deleted = []
    for key, key_value in new_dictionary.items():
        if key_value == value:
            to_be_deleted.append(key)
    for item in to_be_deleted:
        del new_dictionary[item]
    return new_dictionary
