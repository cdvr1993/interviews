
def make_minimum_coin_change(options, target):
  """Returns the combination of minimum coins to reach the target

  Options is a list of the coins available, e.g. [1, 2, 5]
  Target is an integer of the change it has to return
  """

  dp = [[] for i in range(target + 1)]

  for idx in range(1, target + 1):
    for opt in options:
      if opt > idx:
        break

      if len(dp[idx]) == 0 or len(dp[idx]) > len(dp[idx - opt]) + 1:
        dp[idx] = dp[idx - opt] + [opt]

  if sum(dp[-1]) != target:
    # It means it is not possible to reach target with these coins
    return None

  return dp[-1]


def main():
  options = [1, 2, 5]
  target = 30

  result = make_minimum_coin_change(options, target)
  print(result)

  options = [1, 2, 7]
  target = 30

  result = make_minimum_coin_change(options, target)
  print(result)

  options = [3, 7]
  target = 30

  result = make_minimum_coin_change(options, target)
  print(result)

  options = [1, 5]
  target = 9

  result = make_minimum_coin_change(options, target)
  print(result)

if __name__ == '__main__':
  main()
