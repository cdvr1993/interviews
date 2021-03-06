
def make_minimum_coin_change(options, target):
  """Returns the combination of minimum coins to reach the target

  Options is a list of the coins available, e.g. [1, 2, 5]
  Target is an integer of the change it has to return
  """

  result = []
  for coin in sorted(options, reverse=True):
    if target < coin:
      continue

    amount, target = divmod(target, coin)

    result += [coin] * amount

  if target > 0:
    # It can't create the amount
    return None

  return result




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
