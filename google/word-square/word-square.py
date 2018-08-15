import multiprocessing

def get_words(ptr):
    result = []

    def fn(ptr):
        for key in ptr:
            if key == '\0':
                result.extend(ptr[key])
            else:
                fn(ptr[key])
    fn(ptr)

    return result

def prettify(current):
    return '\n'.join(current)

def solve_by_length(words, trie):
    if not words:
        return []

    result = []

    def fn(current):
        if len(current[0]) == len(current):
            result.append(current)
            return

        col = len(current)
        ptr = trie
        for word in current:
            ptr = ptr.get(word[col], {})

        for option in get_words(ptr):
            fn(current + (option,))

    for word in words:
        fn((word,))

    return result


def solve(words):
    tries = {}
    result = []
    words_by_length = {}

    for word in words:
        if len(word) not in tries:
            tries[len(word)] = {}
            words_by_length[len(word)] = []
        ptr = tries[len(word)]
        words_by_length[len(word)].append(word)

        for c in word:
            if c not in ptr:
                ptr[c] = {}
            ptr = ptr[c]

        if c not in ptr:
            ptr[c] = {'\0': []}
        ptr[c]['\0'].append(word)

    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        threads = []
        for length in tries:
            apply = pool.apply_async(solve_by_length, (words_by_length[length], tries[length]))
            threads.append(apply)

        for th in threads:
            result.extend(th.get())

    return result


def main():
    words = ['boy', 'ore', 'yes', 'cat', 'area', 'ball', 'dear', 'lady', 'lead', 'yard']

    result = solve(words)

    print(result)
    print('')
    for item in result:
        print(prettify(item))
        print('')


if __name__ == '__main__':
    main()