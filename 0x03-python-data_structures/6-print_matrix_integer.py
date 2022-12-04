#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    if not rows:
        return None
    columns = len(matrix[0])
    for row in range(rows):
        for column in range(columns):
            print("{:d}".format(matrix[row][column]), end="" if column == columns - 1 else " ")
        print()
