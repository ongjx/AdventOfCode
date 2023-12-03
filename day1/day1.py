
# # data = ['two1nine',
# # 'eightwothree',
# # 'abcone2threexyz',
# # 'xtwone3four',
# # '4nineeightseven2',
# # 'zoneight234',
# # '7pqrstsixteen',
# # 'eighthree']
numberMap = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine': '9'
}

data = []
with open("day1.txt") as f:
    lines = f.readlines()
    for line in lines:
        data.append(line.strip())



total = 0

for word in data:

    first = None
    last = None
    temp = None
    s = ""
    for ch in word:
        if ch.isdigit():
            temp = ch
        else:
            s += ch
            for k,v in numberMap.items():
                print(s, k)
                if s.endswith(k):
                    temp = v
                    print("match", s,k)
        if temp != None:
            last = temp
            if first == None:
                first = last

    total += int(first+last)
    print(first,last)
print(total)
