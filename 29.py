import math

def solve(a):
    ans = 0
    for i in range(len(a)):
        a[i] = a[i] - i
    
    a.sort()

    count = 1
    for i in range(1,len(a)):
        if a[i] == a[i-1]:
            count+=1
        else:
            if count > 1:
                ans += math.perm(count,2)
            count = 1  

    if count != 1:
        ans += math.perm(count,2)

    print(ans//2)

t = int(input())

while t:
    n = int(input())
    a = list(map(int, input().split(" ")))
    solve(a)
    t-=1