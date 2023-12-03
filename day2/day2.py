#part 1
config = {
    'red': 12,
    'green': 13,
    'blue': 14
}
with open('day2.txt') as f:
    data = f.readlines()
    total = 0
    for line in data:
        valid = True
        line = line.strip()
        x = line.split(': ')
        game = x[0].split()[1]

        subset = x[1].split('; ')

        for r in subset:
            colours = r.split(', ')
            for colour in colours:
                y = colour.split(" ")
                c = y[1]
                number = y[0]
                if int(number) > config[c]:
                    valid = False

        if valid:
            total += int(game)
print(total)


#part 2

with open('day2.txt') as f:
    data = f.readlines()
    total = 0
    for line in data:
        tracker = {}

        line = line.strip()
        x = line.split(': ')
        game = x[0].split()[1]

        subset = x[1].split('; ')

        for r in subset:
            colours = r.split(', ')
            for colour in colours:
                y = colour.split(" ")
                c = y[1]
                number = y[0]
                if c not in tracker:
                    tracker[c] = int(number)
                elif int(number) > tracker[c]:
                    tracker[c] = int(number)
        power = 1
        for v in tracker.values():
            power *= v
        total += power
print(total)