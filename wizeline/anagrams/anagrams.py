#!/usr/bin/env python3

def make_anagrams(words):
  d = {}

  for word in words:
    key = ''.join(sorted(word))

    if key not in d:
      # It uses set to remove duplicates
      d[key] = set()

    d[key].add(word)

  return d


def main():
  words = ['cat', 'dog', 'god', 'tca']
  result = make_anagrams(words)

  print(result)

if __name__ == '__main__':
  main()
