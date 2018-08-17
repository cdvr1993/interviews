"""
Your task is to implement the prime video feature to show the current
actors that are on screen when a use pause a video.

You will receive a list of ranges (start, end, actor) and then we will
send some queries with second = ? and you need to return the list of actors
that are on screen in that particular second.
"""


class IntervalTree(object):
    class Node(object):
        def __init__(self, start, end, actor):
            self.start = start
            self.end = end
            self.actor = actor
            self.left = None
            self.right = None

        def __str__(self):
            return '({}, {}) -> {}'.format(
                self.start,
                self.end,
                self.actor
            )

    def __init__(self, onscreen=None):
        self.root = None
        if not onscreen:
            return
        onscreen.sort()
        self.root = self._build_split(onscreen)

    def _build_split(self, onscreen):
        if not onscreen:
            return None

        middle = len(onscreen) >> 1
        node = self.Node(*onscreen[middle])

        for index in range(middle):
            # If overlap split them
            if onscreen[index][1] > node.start:
                onscreen.append((node.start + 1, onscreen[index][1], onscreen[index][2]))
                onscreen[index] = (onscreen[index][0], node.start, onscreen[index][2])

        node.left = self._build_split(onscreen[:middle])
        node.right = self._build_split(sorted(onscreen[middle + 1:]))

        return node

    def query(self, second):
        result = []

        def fn(current):
            if current.start <= second <= current.end:
                result.append(current.actor)
            if second <= current.start:
                if current.left:
                    fn(current.left)
            else:
                if current.right:
                    fn(current.right)

        fn(self.root)

        return result

    def query_performance(self, second):
        """It is only used for performance comparison"""
        result = []
        cycles = [0]

        def fn(current):
            cycles[0] += 1
            if current.start <= second <= current.end:
                result.append(current.actor)
            if second <= current.start:
                if current.left:
                    fn(current.left)
            else:
                if current.right:
                    fn(current.right)

        fn(self.root)
        print(cycles)

        return result

    def preorder(self):
        if not self.root:
            return

        def fn(current, level=0):
            print('L: {}, {}'.format(level, current))

            if current.left:
                fn(current.left, level + 1)
            if current.right:
                fn(current.right, level + 1)

        fn(self.root)


def main():
    onscreen = [
        (1, 55, 'a'),
        (20, 30, 'b'),
        (55, 60, 'b'),
        (15, 30, 'c'),
        (5, 15, 'd'),
        (45, 55, 'c'),
        (15, 45, 'e'),
        (60, 68, 'f'),
        (70, 75, 'g'),
        (72, 80, 'h')
    ]

    it = IntervalTree(onscreen=onscreen)
    it.preorder()

    for i in range(81):
        result = it.query(i)
        print('{}: {}'.format(i, result))

if __name__ == '__main__':
    main()