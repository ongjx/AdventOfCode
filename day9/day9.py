# part1
with open('day9.txt') as f:
  lines = f.readlines()
  all = 0
  for line in lines:
    data = [int(i) for i in line.split(' ')]
    all_diff = [data]

    while True:
      diff_list = []
      for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        diff_list.append(diff)
      if set(diff_list) == {0}:
        break
      else:
        all_diff.append(diff_list)
        data = diff_list
    all_diff.append(diff_list)

    all_diff = all_diff[::-1]
    total = 0
    for i in all_diff:
      last = i[-1]
      total += last
    all += total
  print(all)


#part2


with open('day9.txt') as f:
  lines = f.readlines()
  all = 0
  for line in lines:
    data = [int(i) for i in line.split(' ')]
    all_diff = [data]

    while True:
      diff_list = []
      for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        diff_list.append(diff)
      if set(diff_list) == {0}:
        break
      else:
        all_diff.append(diff_list)
        data = diff_list
    all_diff.append(diff_list)

    all_diff = all_diff[::-1]
    total = 0
    for i in all_diff:
      last = i[0]
      total = last - total
    all += total
  print(all)
