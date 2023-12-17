#part1
import numpy as np

with open('day14/day14.txt') as f:
  data = [line.strip() for line in f.readlines()]

new = []
for i in list(zip(*data)):
  new_row = ["."] * len(i)
  open_spot = 0
  for idx, ch in enumerate(i):
    if ch == '#':
      open_spot = idx + 1
      new_row[idx] = ch
    if ch == 'O':
      new_row[open_spot] = ch
      open_spot += 1
  new.append(new_row)

transpose = np.array(new).T.tolist()

points = len(transpose)
total = 0
for i in transpose:
  total+= i.count('O') * points
  points -= 1
print(total)


with open('day14/day14.txt') as f:
  data = [line.strip() for line in f.readlines()]

def shift(data):
  new = []
  for i in list(zip(*data)):
    new_row = ["."] * len(i)
    open_spot = 0
    for idx, ch in enumerate(i):
      if ch == '#':
        open_spot = idx + 1
        new_row[idx] = ch
      if ch == 'O':
        new_row[open_spot] = ch
        open_spot += 1
    new.append(new_row)
  return np.array(new).T.tolist()

def rotate(x):
  data = x.copy()
  N = len(data)
  for i in range(N//2):
    for j in range(i, N-i-1):
      temp = data[i][j]
      data[i][j] = data[N-1-j][i]
      data[N-1-j][i] = data[N-1-i][N-1-j]
      data[N-1-i][N-1-j] = data[j][N-1-i]
      data[j][N-1-i] = temp
  return data

cache = set(''.join(c for i in data for c in i))
hist = [data]
for i in range(100000000):
  x = shift(data)
  key = ''.join(c for i in x for c in i)

  if key in cache:
    break

  cache.add(key)
  hist.append(x)
  data = rotate(x)

index = hist.index(data)

data = hist[(100000000 - index) % (i - index) + index]
points = len(data)
total = 0
for i in data:
  total+= i.count('O') * points
  points -= 1
print(total)