#!/usr/bin/python3
import sys


def placeQueens(n, row, columns, results):
    if row == n:
        results.append(columns[:])     

    for col in range(n):
        if checkValid(columns, row, col):
            columns[row] = col
            placeQueens(n, row+1, columns, results)

def checkValid(columns, row1, column1):
    for row2 in range(row1):
        if column1 == columns[row2] or abs(columns[row2] - column1) == row1 - row2:
            return False
        return True      

def solveNQueens(n):
    columns = [0] * n
    results = []
    placeQueens(n, 0, columns, results)
    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try: 
        n = int(sys.argv[1])
    except: 
        print("N must be a number")
        exit(1)
    if n < 4: 
        print("N must be at least 4") 
        exit(1)

    ans = solveNQueens(n)
    for sol in ans:
        soln_string = ""
        for i in sol :
            soln_string += str (i + 1) + " "
        print(soln_string.strip())