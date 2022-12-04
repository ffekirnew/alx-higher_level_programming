#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    rs = len(matrix)
    if not rs:
        return None
    cs = len(matrix[0])
    for r in range(rs):
        for c in range(cs):
            print("{:d}".format(matrix[r][c]), end="" if c == cs - 1 else " ")
        print()
