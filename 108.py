t = int(input())

while t:
    t -= 1
    n = int(input())
    arr = []
    f = 0.0
    
    for i in range(n):
        c, p = map(int, input().split())
        arr.append((c, p))

    for i in range(n - 1, -1, -1):
        c, p = arr[i]
        f = max(c + (1.0 - p / 100.0) * f, f)

    print(f"{f:.10f}")