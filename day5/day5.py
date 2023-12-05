#part1

# destination, source, range

# config = {
#     'seed_to_soil': {
#       98: {
#         'destination': 50,
#         'range': 2
#       },
#       50: {
#         'destination': 52,
#         'range': 48
#       }
#     },
#     'soil_to_fertilizer': {
#       15: {
#         'destination': 0,
#         'range': 37
#       },
#       52: {
#         'destination': 37,
#         'range': 2
#       },
#       0: {
#         'destination': 39,
#         'range': 15
#       }
#     },
#     'fertilizer_to_water': {
#       53: {
#         'destination': 49,
#         'range': 8
#       },
#       11: {
#         'destination': 0,
#         'range': 42
#       },
#       0: {
#         'destination': 42,
#         'range': 7
#       },
#       7: {
#         'destination': 57,
#         'range': 4
#       }
#     },
#     'water_to_light': {
#       18: {
#         'destination': 88,
#         'range': 7
#       },
#       25: {
#         'destination': 18,
#         'range': 70
#       },
#     },
#     'light_to_temp': {
#       77: {
#         'destination': 45,
#         'range': 23
#       },
#       45: {
#         'destination': 81,
#         'range': 19
#       },
#       64: {
#         'destination': 68,
#         'range': 13
#       }
#     },
#     'temp_to_humidity': {
#       69: {
#         'destination': 0,
#         'range': 1
#       },
#       0: {
#         'destination': 1,
#         'range': 69
#       },
#     },
#     'humidity_to_location': {
#       56: {
#         'destination': 60,
#         'range': 37
#       },
#       93: {
#         'destination': 56,
#         'range': 4
#       },
#     }
# }

# seeds = [79,14,55,13]
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
