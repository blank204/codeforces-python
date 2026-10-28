n = int(input())

while n:
    n-=1
    t = int(input())
    c = {}

    for i in range(t):
        a = list(map(int, input().split()))
        for j in a:
            c[j] = c.get(j,0) + 1
        
    print("YES" if max(c.values()) <= t*(t-1) else "NO")