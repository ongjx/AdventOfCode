#part1

with open('day11/day11.txt') as f:
  lines = f.readlines()
  galaxy = [line.strip() for line in lines]

emptyr, emptyc = [],[]
for i in range(len(galaxy)):
  if '#' not in galaxy[i]:
    emptyr.append(i)

for c in range(len(galaxy[0])):
  for r in range(len(galaxy)):
    if galaxy[r][c] == '#':
      break
  else:
    emptyc.append(c)

print(emptyr, emptyc)

  # print(data)

  # data
new = []

for r in range(len(galaxy) + len(emptyr)):
  row = []
  for c in range(len(galaxy[0]) + len(emptyc)):
    row.append('.')
  new.append(row)

print(len(new), len(new[0]))

count = 1
addr=0
coords = []
for r in range(len(galaxy)):
  addc=0
  if r in emptyr:
    addr+=1

  for c in range(len(galaxy[0])):
    if c in emptyc:
      addc+=1

    if galaxy[r][c] == '#':
      new[r+addr][c+addc] = str(count)
      coords.append((r+addr, c+addc))
      count += 1

paths = {}
total = 0
for i in range(len(coords)-1):
  l = coords[i+1:]
  # print(coords[i], l)

  for y in l:
    r1,c1 = coords[i]
    r2,c2 = y

    distance = abs(r1-r2) + abs(c1-c2)
    total+= distance

print(total)


#part2

with open('day11/day11.txt') as f:
  lines = f.readlines()
  galaxy = [line.strip() for line in lines]

emptyr, emptyc = [],[]
for i in range(len(galaxy)):
  if '#' not in galaxy[i]:
    emptyr.append(i)

for c in range(len(galaxy[0])):
  for r in range(len(galaxy)):
    if galaxy[r][c] == '#':
      break
  else:
    emptyc.append(c)

print(emptyr, emptyc)

  # print(data)

  # data
new = []

for r in range(len(galaxy) + len(emptyr)):
  row = []
  for c in range(len(galaxy[0]) + len(emptyc)):
    row.append('.')
  new.append(row)

print(len(new), len(new[0]))

count = 1
addr=0
coords = []
for r in range(len(galaxy)):
  addc=0
  if r in emptyr:
    addr+=999999

  for c in range(len(galaxy[0])):
    if c in emptyc:
      addc+=999999

    if galaxy[r][c] == '#':
      # new[r+addr][c+addc] = str(count)
      coords.append((r+addr, c+addc))
      count += 1

paths = {}
total = 0
for i in range(len(coords)-1):
  l = coords[i+1:]
  # print(coords[i], l)

  for y in l:
    r1,c1 = coords[i]
    r2,c2 = y

    distance = abs(r1-r2) + abs(c1-c2)
    total+= distance

print(total)