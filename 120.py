n = int(input())

L= [0] * n
P = [0]*n
for i in range(n):
    c,p = map(int,input().split())
    L[i] = (c,p)
    P[i] = p

L.sort()
P.sort()
for i in range(n):
    if L[i][1] != P[i]:
        print('Happy Alex')
        break
else:
    print('Poor Alex')