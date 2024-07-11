#!/usr/bin/python3
''' solution to the nqueens problem '''
import sys


def backtrack(t, n, cols, pos, neg, board):
    ''' backtrack function to find solution '''
    if t == n:
        res = []
        for h in range(len(board)):
            for r in range(len(board[h])):
                if board[h][r] == 1:
                    res.append([h, r])
        print(res)
        return

    for x in range(n):
        if x in cols or (t + x) in pos or (t - x) in neg:
            continue

        cols.add(x)
        pos.add(t + x)
        neg.add(t - x)
        board[t][x] = 1

        backtrack(t+1, n, cols, pos, neg, board)

        cols.remove(x)
        pos.remove(t + x)
        neg.remove(t - x)
        board[t][x] = 0


def nqueens(n):
    '''
    solution to nqueens problem
    Args:
        n (int): number of queens. Must be >= 4
    Return:
        list of lists representing coordinates of each
        queen for all possible solutions
    '''
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for j in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
