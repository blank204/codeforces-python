n = int(input())
a = set(map(int, input().split()))

print(*(set(range(1,n+1)) - a))