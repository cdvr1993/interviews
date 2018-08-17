"""
You have a List of lists of characters with the following choices:
    - 'O': empty space.
    - 'X': Wall.
    - 'G': there is a guardian.

You have to return the cell that is further from any guardian.

Example:
    [
        ['G', 'O', 'O', 'O'],
        ['X', 'O', 'X', 'X'],
        ['X', 'O', 'O', 'G']
    ]

    The result is 3 (the top right corner) because the distance from (0, 3) to the
    nearest guardian is 3.

Notes:
    [
        ['X', 'O', 'X'],
        ['X', 'X', 'X'],
        ['X', 'O', 'G']
    ]

    - The cell at (0, 1) is invalid because the distance is infinite (there
    is no connection with a guardian).

    - You can only move horizontally and vertically.
"""

import collections
from functools import reduce

def solve(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'G':
                queue = collections.deque([(row, col, 0)])

                while queue:
                    r, c, distance = queue.popleft()

                    options = (
                        (r - 1, c), (r + 1, c),
                        (r, c - 1), (r, c + 1)
                    )

                    next_distance = distance + 1
                    for r1, c1 in options:
                        if (
                            not (0 <= r1 < len(board)) or
                            not (0 <= c1 < len(board[r1])) or
                            (isinstance(board[r1][c1], str) and board[r1][c1] != 'O') or
                            (isinstance(board[r1][c1], int) and next_distance >= board[r1][c1])
                        ):
                            continue

                        board[r1][c1] = next_distance
                        queue.append((r1, c1, next_distance))

    # Finally reduce the board to check the highest number (we have to ignore any char)
    return reduce(
        lambda x, y: max(x, max(0 if isinstance(item, str) else item for item in y)),
        board,
        0
    )


def main():
    board = [
        ['G', 'O', 'O', 'O'],
        ['X', 'O', 'X', 'X'],
        ['X', 'O', 'O', 'G']
    ]
    result = solve(board)
    print(result)

    board = [
        ['X', 'O', 'X'],
        ['X', 'X', 'X'],
        ['O', 'O', 'G']
    ]
    result = solve(board)
    print(result)

if __name__ == '__main__':
    main()