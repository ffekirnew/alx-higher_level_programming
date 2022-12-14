#!/usr/bin/python3
"""Module contains function to divide a matrix by a number."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Parameters
    ----------
    matrix : list[list]
        The matrix to be divided
    div : number
        The number to divide the matrix with

    Returns
    -------
    list[list]
        The matrix after all elements have been divided.

    Raises
    ------
    TypeError
        If div is not a number
    ZeroDivisionError
        If div is zero
    TypeError
        If matrix is not list of lists or rows are not of the same size

    """
    # define error strings
    list_of_lists = 'matrix must be a matrix' + ' (list of lists) of integers/floats'
    division_by_zero = 'division by zero'
    div_must_be_num = 'div must be a number'
    same_size_rows = 'Each row of the matrix must have the same size'

    if type(div) not in [int, float]:
        raise TypeError(div_must_be_num)
    if not div:
        raise ZeroDivisionError(division_by_zero)

    # identify rows and columnss
    rows = len(matrix)
    if type(matrix[0]) is not list:
        raise TypeError(list_of_lists)

    cols = len(matrix[0])

    # iterate over the elements of the matrix and divide them
    for row in range(rows):
        if type(matrix[row]) is not list:
            raise TypeError(list_of_lists)

        if len(matrix[row]) != cols:
            raise TypeError(same_size_rows)

        for col in range(cols):
            if type(matrix[row][col]) not in [int, float]:
                raise TypeError(list_of_lists)
            matrix[row][col] = round(matrix[row][col] / div, 2)

    return matrix
