#part1
l = ['seed_to_soil', 'soil_to_fertilizer', 'fertilizer_to_water', 'water_to_light', 'light_to_temp', 'temp_to_humidity', 'humidity_to_location']

config = {}
with open('day5.txt') as f:
  data = f.readlines()
  data = [x.strip() for x in data if x.strip() != '']
  seeds = [int(i) for i in data[0].split(': ')[1].split(' ')]

  data = data[1:]
  idx = -1

  for i in data:
    if 'map' in i:
      idx += 1
      config[l[idx]] = {}
      next
    else:
      info = i.split(' ')
      destination = int(info[0])
      source = int(info[1])
      r = int(info[2])

      config[l[idx]][source] = {
        'destination': destination,
        'range': r
      }


locs = []
for seed in seeds:
  next_to_find = seed
  for i in l:
    # print("iteration:", i)
    sorted_list = sorted(config[i].keys(), reverse=True)
    # print(sorted_list)
    for j in sorted_list:
      if next_to_find in range(j, j + config[i][j]['range']):
        next_to_find = next_to_find - j + config[i][j]['destination']
        # print('found submatch. Source:', j, 'Destination: ', config[i][j]['destination'], 'Next to find:', next_to_find)
        break
    else:
      next_to_find = next_to_find
  locs.append(next_to_find)
print(min(locs))

#part 2

new = {}
seeds = []
with open('day5.txt') as f:
  data = f.readlines()
  data = [x.strip() for x in data if x.strip() != '']
  x = [int(i) for i in data[0].split(': ')[1].split(' ')]

  for i in range(0,len(x), 2):
    seeds.append((x[i], x[i]+ x[i+1]))

for i in l:
  new = []
  while len(seeds) > 0:
    start, end = seeds.pop()
    for k,v in config[i].items():
      s = k
      d = v['destination']
      r = v['range']

      intervalStart = max(start, s)
      intervalEnd = min(end, s+r)

      if intervalStart < intervalEnd:
        print(intervalStart, intervalEnd)
        new.append((intervalStart - s + d, intervalEnd - s + d))
        if intervalStart > start:
          seeds.append((start, intervalStart))
        if end > intervalEnd:
          seeds.append((intervalEnd, end))
        break
    else:
      new.append((start, end))
  seeds = new
print(min(seeds)[0])