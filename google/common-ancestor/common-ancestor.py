"""
The function will receive two children and we need to find the common
ancestor.

Assumption: There is always a common ancestor.
"""


class Person(object):
    def __init__(self, label, parent):
        self.parent = parent
        self.label = label

    def __str__(self):
        return 'I: {} - Parent: {}'.format(self.label, self.parent.label if self.parent else None)


def solve(child1, child2):
    visited = set()

    def up(child1, child2):
        if child1 is child2:
            return child1
        if child1 in visited:
            return child1
        if child2 in visited:
            return child2

        p1, p2 = None, None
        if child1:
            p1 = child1.parent
            visited.add(child1)
        if child2:
            p2 = child2.parent
            visited.add(child2)

        return up(p1, p2)

    return up(child1, child2)



def main():
    first_human = Person('a', None)

    child1 = Person('d', Person('c', Person('b', first_human)))
    child2 = Person('g', Person('f', Person('e', first_human)))
    result = solve(child1, child2)
    print(result)

    child1 = Person('d', Person('c', Person('b', first_human)))
    child2 = Person('f', Person('e', child1.parent))
    result = solve(child1, child2)
    print(result)

    child1 = Person('f', Person('e', Person('d', Person('c', Person('b', first_human)))))
    child2 = Person('i', Person('h', Person('g', child1.parent.parent.parent.parent)))
    result = solve(child1, child2)
    print(result)

if __name__ == '__main__':
    main()