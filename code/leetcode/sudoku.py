"""Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition."""
from collections import defaultdict


def isValidSudoku(board: list[list[str]]) -> bool:
    columDict = defaultdict(list)
    rowDict = defaultdict(list)
    square = defaultdict(list)
    for colum in range(9):
        for row in range(9):
            element = board[row][colum]
            if element == ".":
                continue
            if element in rowDict[row] or element in columDict[colum] or element in square[(row//3, colum//3)]:
                return False
            rowDict[row].append(element)
            columDict[colum].append(element)
            square[(row//3, colum//3)].append(element)
    return True


input = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(input))