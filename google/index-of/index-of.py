"""
Implement string index of function
"""

def indexOf(source, pattern):
    swaps = [1] * (len(pattern) + 1)
    current_swap = 1

    for index in range(len(pattern)):
        while current_swap <= index and pattern[index] != pattern[index - current_swap]:
            current_swap += 1
        swaps[index + 1] = current_swap

    start = 0
    length = 0
    for char in source:
        while length >= 0 and pattern[length] != char:
            start += swaps[length]
            length -= swaps[length]

        length += 1

        if length == len(pattern):
            return start

    return -1

def main():
    source = 'Hello world'
    pattern = 'or'
    index = indexOf(source, pattern)
    print(index)

if __name__ == '__main__':
    main()