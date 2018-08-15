class Iterator2D(object):
    def __init__(self, lists):
        self._lists = lists
        self._prev = (-1, -1)
        self._current = (0, -1)

    def __iter__(self):
        return self

    def _next_index(self):
        r, c = self._current

        while r < len(self._lists):
            c += 1
            if c < len(self._lists[r]):
                break
            else:
                c = -1
                r += 1

        return (r, c)

    def has_next(self):
        r, c = self._next_index()

        return 0 <= r < len(self._lists) and 0 <= c < len(self._lists[r])

    def __next__(self):
        if self.has_next():
            self._prev = self._current
            self._current = self._next_index()
            return self._lists[self._current[0]][self._current[1]]
        raise StopIteration()

    def remove(self):
        """Removes the element at current position

        It is not possible to call this before next() and more than one time
        for each call.
        """

        if self._current == self._prev or self._current[1] == -1:
            return

        del self._lists[self._current[0]][self._current[1]]
        self._current = self._prev

        if self._current[0] == -1:
            self._current = (0, -1)


def test_iterator():
    lists = [ [1,2,3], [], [], [4,5], [6], [7,8,9,10] ]
    it = Iterator2D(lists)

    for item in it:
        print(item)

    print(it._lists)

def test_iterator_remove():
    lists = [ [1,2,3], [], [], [4,5], [6], [7,8,9,10] ]
    it = Iterator2D(lists)

    # This calls does not affect
    it.remove()
    it.remove()
    it.remove()

    for item in it:
        it.remove()
        # The second call does not affect
        it.remove()
        print(item)

    # At the end the list is empty
    print(it._lists)


def main():
    test_iterator()
    test_iterator_remove()

if __name__ == '__main__':
    main()