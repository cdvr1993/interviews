"""
The task is to retrieve the top N elements from a very big list of numbers. So
the first part is how we can handle a very big list of numbers that does not
fit into memory, for this we are going to use an iterator to do lazy loading.
Then how do we handle top N numbers, for this we are going to use a heap, but
we are going to use a min heap to store only N numbers and not all of them.

Notes:
    - The numbers.txt file it is not big enough to fill the entire memory, but
      we are going to assume that it does.
    - It only works in python3
"""

import heapq
from os import path


class FileIterator(object):
    def __init__(self, filename):
        self._filename = filename
        self._fdesc = None

    def __iter__(self):
        self._fdesc = open(self._filename)
        return self

    def __next__(self):
        line = self._fdesc.readline()

        if line:
            return int(line.replace('\n', ''))

        raise StopIteration()


def top_n(filename, n):
    heap = []

    for number in FileIterator(filename):
        if len(heap) < n:
            heapq.heappush(heap, number)
        elif number > heap[0]:
            heapq.heappushpop(heap, number)

    return [heapq.heappop(heap) for _ in range(n)][::-1]


def main():
    filename = path.join(path.dirname(__file__), 'numbers.txt')
    n = 10
    result = top_n(filename, n)
    print(result)

if __name__ == '__main__':
    main()
