#part1

config = {}

with open('day8.txt') as f:
  data = f.readlines()
  instructions = data[0].strip()
  data = data[2:]
  for i in data:
    key, value = i.strip().split(' = ')
    value = value.split(", ")
    lv,rv = value[0][1:], value[1][:-1]
    config[key] = {
      'L': lv,
      'R': rv
    }

# print(config)

next = "AAA"
found = False
steps = 1
while not found:
  for i in instructions:
    if config[next][i] != 'ZZZ':
      next = config[next][i]
      steps += 1
    else:
      found = True
      break

print(steps)

#part2
## reddit help..
# nodes = list(filter(lambda x: x[2] == 'A', config.keys()))
# nextNodes = nodes
# print(nextNodes)
# found = False
# steps = 1
# while not found:
#   for i in instructions:
#     currentNodes = []
#     for node in nextNodes:
#       currentNodes.append(config[node][i])
#     # print('ends with z list', list(filter(lambda x: x[2] == 'Z', currentNodes)))
#     # print('current nodes', currentNodes)
#     if (len(list(filter(lambda x: x[2] == 'Z', currentNodes))) == len(nodes)):
#       found=True
#       break
#     else:
#       steps += 1
#       nextNodes = currentNodes
#     print(steps)


from math import gcd

steps, _, *rest = open('day8.txt').read().splitlines()

network = {}

for line in rest:
    pos, targets = line.split(" = ")
    network[pos] = targets[1:-1].split(", ")

positions = [key for key in network if key.endswith("A")]
cycles = []

for current in positions:
    cycle = []

    current_steps = steps
    step_count = 0
    first_z = None

    while True:
        while step_count == 0 or not current.endswith("Z"):
            step_count += 1
            current = network[current][0 if current_steps[0] == "L" else 1]
            current_steps = current_steps[1:] + current_steps[0]

        cycle.append(step_count)

        if first_z is None:
            first_z = current
            step_count = 0
        elif current == first_z:
            break

    cycles.append(cycle)

nums = [cycle[0] for cycle in cycles]

lcm = nums.pop()

for num in nums:
    lcm = lcm * num // gcd(lcm, num)

print(lcm)

