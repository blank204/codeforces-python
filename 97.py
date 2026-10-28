n,t = map(int, input().split())
a = list(map(int, input().split()))
t1 = 0
t-=1

while t1 <= t: 
    if t1 == t:
        print("YES")
        quit()
    
    t1 += a[t1]

print("NO")
