#part 1
output = {}
with open('day7.txt') as f:
  data = f.readlines()
  output = []
  for i in data:
    hand, bid = i.strip().split(' ')
    output.append((hand, bid))


order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

config = {
  1: [],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: []
}
for out in output:
  hand, bid = out

  if len(set(hand)) == len(hand):
    config[1].append([hand, bid])
  if len(set(hand)) == 1:
    config[7].append([hand, bid])

  pairs = 0
  threeOfAKind = False
  fullHouse = False
  for i in set(hand):
    if hand.count(i) == 4:
      config[6].append([hand, bid])
    if hand.count(i) == 2:
      pairs += 1
    if hand.count(i) == 3:
      threeOfAKind = True
    if threeOfAKind and pairs == 1:
      fullHouse = True

  if pairs == 2:
    config[3].append([hand, bid])
  if fullHouse:
    config[5].append([hand, bid])
  elif threeOfAKind:
    config[4].append([hand, bid])
  elif pairs == 1:
    config[2].append([hand, bid])

def comparator(a,b):
  for i in range(len(a[0])):
    if order.index(a[0][i]) > order.index(b[0][i]):
      return -1
    elif order.index(a[0][i]) < order.index(b[0][i]):
      return 1
  return 0


from functools import cmp_to_key
rank = 1
total = 0
for k, v in config.items():
  v = sorted(v, key=cmp_to_key(comparator))
  config[k] = v
  for i in v:
    value = rank * int(i[1])
    total += value
    rank += 1


print(total)

#part 2

order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
exclude = set("J")
config = {
  1: [],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: []
}
count = 0
for out in output:
  hand, bid = out
  newhand = ''.join(i for i in hand if i != 'J' )
  numJokers = hand.count('J')

  pairs = 0
  threeOfAKind = False
  fullHouse = False
  fourOfAKind = False
  fiveOfAKind = False

  for i in set(newhand):
    if hand.count(i) == 2:
      pairs += 1
      if pairs == 1 and threeOfAKind:
        fullHouse = True
    elif hand.count(i) == 3:
      threeOfAKind = True
      if threeOfAKind and pairs == 1:
        fullHouse = True
    elif hand.count(i) == 4:
      fourOfAKind = True
    elif hand.count(i) == 5:
      fiveOfAKind = True

  if fiveOfAKind:
    config[7].append([hand, bid])
  elif fourOfAKind:
    if numJokers == 1:
      config[7].append([hand, bid])
    else:
      config[6].append([hand, bid])
  elif fullHouse:
    config[5].append([hand, bid])
  elif threeOfAKind:
    if numJokers == 2:
      config[7].append([hand, bid])
    elif numJokers == 1:
      config[6].append([hand, bid])
    else:
      config[4].append([hand, bid])
  elif pairs == 2:
    if numJokers == 1:
      config[5].append([hand, bid])
    else:
      config[3].append([hand, bid])
  elif pairs == 1:
    if numJokers == 3:
      config[7].append([hand, bid])
    elif numJokers == 2:
      config[6].append([hand, bid])
    elif numJokers == 1:
      config[4].append([hand, bid])
    else:
      config[2].append([hand, bid])
  else:
    if numJokers == 5:
      config[7].append([hand, bid])
    elif numJokers == 4:
      config[7].append([hand, bid])
    elif numJokers == 3:
      config[6].append([hand, bid])
    elif numJokers == 2:
      config[4].append([hand, bid])
    elif numJokers == 1:
      config[2].append([hand, bid])
    else:
      config[1].append([hand, bid])


found = {}
rank = 1
total = 0
for k, v in config.items():
  v = sorted(v, key=cmp_to_key(comparator))
  config[k] = v
  for i in v:
    value = rank * int(i[1])
    total += value
    rank += 1


x = []
for k, v in config.items():
   for i in v:
      x.append((i[0], i[1]))

print(total)

