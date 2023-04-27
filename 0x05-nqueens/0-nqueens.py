#!/usr/bin/python3
"""
NQueens Solver
"""
import sys


def checksValid(board, row, col):
    """Checks if position is valid
    """
    b_size = len(board)
    if sum(board[row]) or sum([board[i][col] for i in range(b_size)]) != 0:
        return False

    for i, j in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
        r, c = row, col
        while 0 <= r + i < b_size and 0 <= c + j < b_size:
            r, c = r + i, c + j
            if board[r][c]:
                return False
    return True


def solution_queens(board, row, solutions):
    """Solves the nqueens problem
    :param board: board
    :param row: row
    :param solutions: solutions
    """
    n = len(board)
    if row == n:
        solutions.append([[r, board[r].index(1)] for r in range(n)])
        return

    for col in range(n):
        if checksValid(board, row, col):
            board[row][col] = 1
            solution_queens(board, row + 1, solutions)
            board[row][col] = 0


def print_sol(n):
    """Prints the solutions
    """
    board = [[0 for col in range(n)] for row in range(n)]
    solutions = []
    solution_queens(board, 0, solutions)
    for row in solutions:
        print(row)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print('N must be at least 4')
            sys.exit(1)
        print_sol(n)

    except ValueError:
        print('N must be a number')
        sys.exit(1)
