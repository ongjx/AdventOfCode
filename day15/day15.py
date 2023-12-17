#part1

with open('day15/day15.txt') as f:
  data = f.readline().split(',')

total = 0
for i in data:
  currVal = 0
  for ch in i:
    currVal += ord(ch)
    currVal *= 17
    currVal %= 256
  total += currVal

print(total)

#part2
with open('day15/day15.txt') as f:
  data = f.readline().split(',')

boxes = [[] for i in range(256)]

focal = {}

def hash(i):
  currVal = 0
  for ch in i:
    currVal += ord(ch)
    currVal *= 17
    currVal %= 256
  return currVal

for i in data:

    if '-' in i:
      box = i[:-1]
      boxNum = hash(box)
      if box in focal:
        boxes[boxNum].remove(f"{box} {focal[box]}")
        del focal[box]

    if "=" in i:
      box, fLen = i.split("=")
      boxNum = hash(box)
      if box in focal:
        idx = boxes[boxNum].index(f"{box} {focal[box]}")
        boxes[boxNum][idx] = f"{box} {fLen}"
        focal[box] = fLen
      else:
        focal[box] = fLen
        boxes[boxNum].append(f"{box} {fLen}")

total = 0
for i, box in enumerate(boxes):
  for j, focal in enumerate(box):
    # print((1+i+1),  j+1, int(focal.split(' ')[1]))
    total += (1+i) * (j+1) * int(focal.split(' ')[1])

print(total)