"""
A monkey is trying to cross a river, he can jump at most max_jump spaces. At
the beggining all the stones are hidden by the water but the water is
constantly changing. The task is to return the minimum time needed to get
to the pther side of the river.

Notes:
    - The monkey starts at position -1.

Example:
stones = [1, -1, 0, 2, 3, 5]
max_jumps = 3

Symbols:
    - R means a rock

Position 6 is the other side of the river

time    Position
        -1 0 1 2 3 4 5 6
0              R
1          R   R
2          R   R R

At time = 2, the monkey jumps from -1 to 0, then from 0 to 3. Finally
from to it jumps to the other side of the river (because 3 + max_jumps[3] is 6).
"""

def minimum_time_to_cross(stones, max_jump):
    # It means it is not possible to reach the other side of the river
    for i in range(len(stones) - max_jump, len(stones)):
        if stones[i] != -1:
            break
    else:
        return -1

    def cross(time, start):
        if start + max_jump >= len(stones):
            return True

        for index in range(start + 1, min(start + max_jump + 1, len(stones))):
            if 0 <= stones[index] <= time and cross(time, index):
                return True
        return False

    time = 0

    while True:
        if cross(time, -1):
            return time
        time += 1


def main():
    stones = [1, -1, 0, 2, 3, 5]
    max_jump = 3
    result = minimum_time_to_cross(stones, max_jump)
    print(result)

    stones = [3, 2, 1]
    max_jump = 1
    result = minimum_time_to_cross(stones, max_jump)
    print(result)

    stones = [1, 2, 3, 4, -1, -1, -1]
    max_jump = 3
    result = minimum_time_to_cross(stones, max_jump)
    print(result)

if __name__ == '__main__':
    main()