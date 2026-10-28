import math

n = int(input())
a = list(map(int, input().split()))
d = {1:0, 2:0, 3:0, 4:0}

for i in a:
    d[i] += 1

count = d[4]

pair = min(d[3], d[1])
count += d[3] 
d[1] -= pair

count += d[2] // 2
d[2] %= 2

if d[2] == 1:
    count += 1
    d[1] -= min(2, d[1])

if d[1] > 0:
    count += math.ceil(d[1] / 4)

print(count)