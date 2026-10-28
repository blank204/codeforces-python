def solve(a):
    b = a.sort()
    print("YES" if a[0]+a[1]==a[2] else "NO")

n = int(input())

while n:
    a = list(map(int, input().split(" ")))
    solve(a)
    n-=1
