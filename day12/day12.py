#part1

with open('day12/day12.txt') as f:
  data = [line.strip() for line in f.readlines()]
print(data)


def count(cfg, nums):
  #invalid cases
  if cfg == "":
    return 1 if nums == () else 0
  if nums == ():
    return 0 if '#' in cfg else 1

  #valid cases
  result = 0
  if cfg[0] in '.?':
    result += count(cfg[1:], nums)
  if cfg[0] in '#?':
    if nums[0] <= len(cfg) and '.' not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != '#'):
      result += count(cfg[nums[0]+1:], nums[1:])
  return result

total = 0
for i in data:
  cfg, nums = i.split()
  nums = tuple(map(int, nums.split(',')))
  print(cfg)
  total += count(cfg,nums)

print(total)