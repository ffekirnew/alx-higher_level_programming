#!/usr/bin/python3


def roman_to_int(roman_string):
    s = roman_string
    converted = 0
    conversion_key = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    i = 0
    while i < len(s):
        add = 0
        if i < len(s) - 1:
            if (s[i] == 'I') and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                add = 4 if s[i + 1] == 'V' else 9
                i += 2
            elif (s[i] == 'X') and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                add = 40 if s[i + 1] == 'L' else 90
                i += 2
            elif (s[i] == 'C') and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                add = 400 if s[i + 1] == 'D' else 900
                i += 2
            else:
                add = conversion_key[s[i]]
                i += 1
        else:
            add = conversion_key[s[i]]
            i += 1
        converted += add
    return converted
