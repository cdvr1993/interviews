"""
Return the order in which we need to build these dependencies.
Also check if there is a cycle in the dependencies.
"""

import collections

def order(targets, dependencies):
    result = collections.OrderedDict()
    visited = set()

    restrictions = {}
    for a, depends_on in dependencies:
        if a not in restrictions:
            restrictions[a] = set()

        restrictions[a].add(depends_on)

    def fn(current):
        for dep in restrictions.get(current, []):
            if dep in visited:
                if dep not in result:
                    raise Exception('Cycle detected')
                continue

            visited.add(dep)
            fn(dep)

        result[current] = None

    for target in targets:
        if target in visited:
            continue

        visited.add(target)
        fn(target)

    return list(result)


def main():
    targets = ('a', 'b', 'c', 'd')
    dependencies = (('a', 'b'), ('c', 'd'))
    result = order(targets, dependencies)
    print(result)

    targets = ('a', 'b', 'c', 'd')
    dependencies = (('a', 'c'), ('b', 'c'))
    result = order(targets, dependencies)
    print(result)

    targets = ('a', 'b', 'c')
    dependencies = (('a', 'b'), ('b', 'c'), ('c', 'a'))
    result = order(targets, dependencies)
    print(result)

if __name__ == '__main__':
    main()