a = []
x = 0
y = 0

for i in range(5):
    a.append(list(map(int, input().split(" "))))
    if 1 in a[i]: x = abs(2- a[i].index(1)); y = abs(2-i)

print(x+y)