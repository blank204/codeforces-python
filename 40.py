n = int(input())
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))
c = []

for i in range(1,len(a)):
    c.append(a[i])

for i in range(1,len(b)):
    c.append(b[i])

if len(set(c)) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")