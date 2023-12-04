#part 1
points = 0
with open('day4.txt') as f:
    data = f.readlines()
    for line in data:
        line = line.strip()
        x = line.split(': ')
        game = x[0].split()[1]

        subset = x[1].split(' | ')

        winning = subset[0].split(' ')
        numbers = subset[1].split(' ')

        score = 0
        count = 0
        for i in numbers:
            if i.strip() in winning and i.strip().isdigit():
                count += 1
        if count != 0:
            points += 2**(count-1)
print(points)

#part 2

config = {}
with open('day4.txt') as f:
    data = f.readlines()
    for line in data:
        line = line.strip()
        x = line.split(': ')
        game = x[0].split()[1]
        subset = x[1].split(' | ')

        winning = subset[0].split(' ')
        numbers = subset[1].split(' ')
        matches = 0

        if int(game) not in config:
            config[int(game)] = 1
        else:
            config[int(game)] += 1

        copies = config[int(game)]

        for i in numbers:
            if i.strip().isdigit():
                if i in winning:
                    matches += 1

        for i in range(matches):
            if int(game)+i+1 not in config:
                config[int(game)+i+1] = copies
            else:
                config[int(game)+i+1] += copies

total = 0
for v in config.values():
    total += v
print(total)