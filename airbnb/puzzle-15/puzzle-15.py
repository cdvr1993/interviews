import collections
import random

class Board(object):
    def __init__(self, n):
        self.n = n
        self.matrix = [['0'] * n for _ in range(n)]

        self.correct_answer = '|'.join([str(i) for i in range(1, n ** 2)] + ['0'])

        choices = {str(i) for i in range(0, n ** 2)}

        for row in range(len(self.matrix)):
            for column in range(len(self.matrix[row])):
                value = random.choice(list(choices))
                self.matrix[row][column] = value
                choices.remove(value)

    def copy_board(self):
        return [_list[:] for _list in self.matrix]

    def hash_matrix(self, matrix):
        return '|'.join('|'.join(_list) for _list in matrix)

    def solve(self):
        visited = {self.hash_matrix(self.matrix)}
        queue = collections.deque([(self.matrix, (self.n - 1, self.n - 1))])

        if self.correct_answer in visited:
            return

        while queue:
            self.matrix, (row, col) = queue.popleft()

            options = (
                (row - 1, col),
                (row, col - 1),
                (row, col + 1),
                (row + 1, col)
            )

            for r, c in options:
                if not (0 <= r < self.n) or not (0 <= c < self.n):
                    continue

                matrix = self.copy_board()

                # Swap elements
                matrix[row][col], matrix[r][c] = matrix[r][c], matrix[row][col]
                key = self.hash_matrix(matrix)

                if key in visited:
                    continue

                if key == self.correct_answer:
                    self.matrix = matrix
                    return

                visited.add(key)
                queue.append((matrix, (r, c)))

        raise Exception('Not solvable')

    def __repr__(self):
        return repr(self.matrix)


def main():
    board = Board(4)
    print(board)
    board.solve()
    print(board)

if __name__ == '__main__':
    main()