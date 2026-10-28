n = int(input())
a = sorted(list(map(int, input().split())))
q = int(input())
d = {}

for i in a:
    d[i] = d.get(i,0) + 1

