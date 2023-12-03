# part 1
config = {}
with open('day3.txt') as f:
    data = f.readlines()
    total = 0
    for row in range(len(data)):
        data[row] = data[row].strip()
        start = 0
        end = 1
        for col in range(len(data[row])):
            if not data[row][col].isdigit():
                if data[row][start:end].isdigit():
                    for i in range(start,end):
                        config[(row, i)] = int(data[row][start:end])
                    # config[(row, col)] = int(data[row][start:end])
                start = col+1
                end = start + 1
            else:
                end = col + 1
        if data[row][start:end].isdigit():
            for i in range(start,end):
                config[(row, i)] = int(data[row][start:end])
            # config[(row, col)] = int(data[row][start:end])

    total = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            val = data[row][col]
            if not val.isdigit() and val != '.':

                if data[row-1][col] == '.':
                    if (row-1,col-1) in config:
                        total += config[(row-1,col-1)]
                    if (row-1,col+1) in config:
                        total += config[(row-1,col+1)]
                else:
                    total += config[(row-1,col)]


                if (row,col-1) in config:
                    total += config[(row,col-1)]
                if (row,col+1) in config:
                    total += config[(row,col+1)]

                if data[row+1][col] == '.':
                    if (row+1,col-1) in config:
                        total += config[(row+1,col-1)]
                    if (row+1,col+1) in config:
                        total += config[(row+1,col+1)]
                else:
                    total += config[(row+1,col)]

# print(total)
# print (config)
# part 2
config = {}
with open('day3.txt') as f:
    data = f.readlines()
    total = 0
    for row in range(len(data)):
        data[row] = data[row].strip()
        start = 0
        end = 1
        for col in range(len(data[row])):
            if not data[row][col].isdigit():
                if data[row][start:end].isdigit():
                    for i in range(start,end):
                        config[(row, i)] = int(data[row][start:end])
                start = col+1
                end = start + 1
            else:
                end = col + 1
        if data[row][start:end].isdigit():
            for i in range(start,end):
                config[(row, i)] = int(data[row][start:end])

    total = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            val1 = None
            val2 = None
            val = data[row][col]
            if val != '*':
                next
            else:
                if data[row-1][col] == '.':
                    if (row-1,col-1) in config:
                        if val1 == None:
                            val1 = config[(row-1,col-1)]
                        elif val2 == None:
                            val2 = config[(row-1,col-1)]
                        else:
                            next

                    if (row-1,col+1) in config:
                        if val1 == None:
                            val1 = config[(row-1,col+1)]
                        elif val2 == None:
                            val2 = config[(row-1,col+1)]
                        else:
                            next
                else:
                    if val1 == None:
                            val1 = config[(row-1,col)]
                    elif val2 == None:
                        val2 = config[(row-1,col)]
                    else:
                        next


                if (row,col-1) in config:
                    if val1 == None:
                            val1 = config[(row,col-1)]
                    elif val2 == None:
                        val2 = config[(row,col-1)]
                    else:
                        next

                if (row,col+1) in config:
                    if val1 == None:
                            val1 = config[(row,col+1)]
                    elif val2 == None:
                        val2 = config[(row,col+1)]
                    else:
                        next

                if data[row+1][col] == '.':
                    if (row+1,col-1) in config:
                        if val1 == None:
                            val1 = config[(row+1,col-1)]
                        elif val2 == None:
                            val2 = config[(row+1,col-1)]
                        else:
                            next
                    if (row+1,col+1) in config:
                        if val1 == None:
                            val1 = config[(row+1,col+1)]
                        elif val2 == None:
                            val2 = config[(row+1,col+1)]
                        else:
                            next
                else:
                    if val1 == None:
                        val1 = config[(row+1,col)]
                    elif val2 == None:
                        val2 = config[(row+1,col)]
                    else:
                        next
                if val1 != None and val2 != None:
                    multiply = val1 * val2
                    total += multiply

print(total)
