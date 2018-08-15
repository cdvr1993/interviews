"""We need to form two teams following the restrictions of the preferences of
each person. For instance restrictions = [ (0, 1) ] means that `0` must not work
with `1`. If there is no configuration possible raise an Exception."""

import collections

def make_teams(n, restrictions):
    teams = (set(), set())
    inv_deps = collections.defaultdict(set)

    for a, b in restrictions:
        inv_deps[a].add(b)
        inv_deps[b].add(a)

    visited = set()

    def fn(person, index_team):
        visited.add(person)

        next_index = (index_team + 1) % len(teams)
        for another in inv_deps[person]:
            if another not in visited:
                fn(another, next_index)
            elif another in teams[index_team]:
                raise Exception('No configuration possible')

        teams[index_team].add(person)

    for person in range(n):
        if person not in visited:
            fn(person, 0)

    return teams


def main():
    # result = ({0, 2, 3, 4, 5}, {1})
    n = 6
    restrictions = [(0, 1)]
    result = make_teams(n, restrictions)
    print(result)

    # result = ({0, 2, 5}, {1, 3, 4})
    n = 6
    restrictions = [(0, 1), (4, 0), (5, 1), (2, 3)]
    result = make_teams(n, restrictions)
    print(result)

    # Exception
    n = 6
    restrictions = [(0, 1), (5, 1), (2, 3), (0, 2), (0, 3)]
    result = make_teams(n, restrictions)
    print(result)

if __name__ == '__main__':
    main()