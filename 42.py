n = int(input())
a = list(map(int, input().split(" ")))

maxx = a.index(max(a))
minn = a[::-1].index(min(a))

print(maxx+minn-1 if maxx > n-1-minn else maxx+minn)
