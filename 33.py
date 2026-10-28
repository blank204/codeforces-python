n = int(input())
a = list(map(int, input().split(" ")))
p = [0]*n

for i in range(n):
    p[a[i]-1] = i+1
print(*p)
