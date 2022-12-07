#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    answer = []
    for i in range(len(matrix)):
        answer.append([])
        for j in range(len(matrix[i])):
            answer[-1].append(matrix[i][j])
    return answer
