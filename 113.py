t = int(input())

while t:
    t-=1

    a,b,n = map(int, input().split())
    arr = list(map(int, input().split()))
    
    sol = b
    for i in arr:
        sol += min(i,a-1)

    print(sol)