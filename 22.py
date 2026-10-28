import math
a = int(input())
b = []

for i in range(a):
    b.append(tuple(map(int, input().split())))

cap = 0
m = 0

for i in b:
    cap += i[1] - i[0]
    m = max(cap,m)

print(m)
