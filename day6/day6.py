with open('day6.txt') as f:
  data = f.readlines()
  output = []
  for i in data:
    for j in i.split(' '):
      if j.strip() != "":
        output.append(j.strip())


time = []
distance = []
for i in range(1, len(output)//2):
  time.append(int(output[i]))
  distance.append(int(output[i+len(output)//2]))

total = 0
for i in range(len(time)):
  wins = 0
  for j in range(1, time[i]+1):
    distanceTravelled = j * (time[i] - j)
    if distanceTravelled > distance[i]:
      total += 1

print(total)