"""
This version is slightly better when there is a lot of guardians which are
neighbors. Because there is no point on continue iterating over empty space
which we already know it is a neighbor of a guardian.
"""

import collections
from functools import reduce

def solve(board, log=False):
    cycles = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'G':
                board[row][col] = 0
                queue = collections.deque([(row, col, 0)])

                while queue:
                    r, c, distance = queue.popleft()

                    cycles += 1

                    options = (
                        (r - 1, c), (r + 1, c),
                        (r, c - 1), (r, c + 1)
                    )

                    next_distance = distance + 1
                    additions = []
                    guardian_found = False
                    for r1, c1 in options:
                        if (
                            not (0 <= r1 < len(board)) or
                            not (0 <= c1 < len(board[r1])) or
                            (isinstance(board[r1][c1], int) and next_distance >= board[r1][c1]) or
                            board[r1][c1] == 'X'
                        ):
                            continue

                        if board[r1][c1] == 'G':
                            guardian_found = True
                            continue

                        board[r1][c1] = next_distance
                        additions.append((r1, c1, next_distance))
                    if not guardian_found:
                        queue.extend(additions)
            else:
                cycles += 1

    if log:
        print('Cycles: {}'.format(cycles))

    # Finally reduce the board to check the highest number (we have to ignore any char)
    return reduce(
        lambda x, y: max(x, max(0 if isinstance(item, str) else item for item in y)),
        board,
        0
    )


def main():

    # To prove that we should not add neighbors of a guardian.
    # (0, 0) will add (0, 1) but no [(1, 1), (2, 1)] because there are
    # guardians next to them.
    board = [
        ['G', 'O', 'G', 'X'],
        ['G', 'O', 'G', 'X'],
        ['G', 'O', 'O', 'O'],
        ['G', 'G', 'G', 'X']
    ]
    result = solve(board, True)
    print(result)

if __name__ == '__main__':
    main()