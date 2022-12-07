#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    answer = []
    for i in range(len(matrix)):
        answer.append(list(map(lambda x: x ** 2, matrix[i])))
    return answer
