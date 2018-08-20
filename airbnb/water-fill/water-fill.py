"""
The task consists on returning a matrix in how a container will be filled
after throwing some amount of water at a specific position.

The input parameters are:
    - Array of heights for each segment of the container.
    - Water amount (Each cell will be filled with one unit of this)
    - Index which we will throw water

The matrix have two code characters:
    - X for soil.
    - W for water.

In order to assign one unit of water there must be soil on both sides of the empty space.
For instance:
    X X                             XWX
    XXX  , So we can assign water   XXX

Also you need to check how the water will fill depending on the index in which
we throw water. For instance:

  I   ->  If I throw one unit of water there
X    X
X  X X
X XXXX
XXXXXX

This will be filled:

X    X
X  X X
XWXXXX
XXXXXX

Instead of

X    X
X WX X
X XXXX
XXXXXX

Assumptions:
- You may assume the minimum height is 1, because we always have soil at the bottom.
- There is less water than empty spaces sorrounded by soil.
"""


def solve(heights, water, water_index):
    size = max(heights)
    matrix = [['X' if heights[col] > row else ' ' for col in range(len(heights))] for row in range(size)]

    print_rev_matrix(matrix)

    index = water_index

    # While there is water left to throw
    while water > 0:
        # We need to find the correct empty space to drop the water
        min_index = index

        # We move to the right to find the index of the minimum height
        while index < len(heights) and heights[index] >= heights[index + 1]:
            if heights[index + 1] < heights[min_index]:
                min_index = index + 1
            index += 1

        # Then we move to the left
        while index > 0 and heights[index - 1] <= heights[index]:
            if heights[index - 1] < heights[min_index]:
                min_index = index - 1
            index -= 1

        # We have found the index of the minimum height, so we fill that space
        matrix[heights[min_index]][min_index] = 'W'

        # We increase the height of that position
        heights[min_index] += 1
        water -= 1

    return matrix


def print_rev_matrix(matrix):
    print('\n'.join(''.join(_list) for _list in reversed(matrix)))


def main():
    heights = [4,1,2,3,2,4]
    water = 4
    water_index = 2
    result = solve(heights, water, water_index)
    print('')
    print_rev_matrix(result)

    heights = [4,1,2,3,2,4]
    water = 8
    water_index = 2
    result = solve(heights, water, water_index)
    print('')
    print_rev_matrix(result)

if __name__ == '__main__':
    main()