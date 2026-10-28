n = int(input())
a = []
while(n):
    a.append(input())
    n-=1

grp = 1

for i in range(1,len(a)):
    if a[i][0] == a[i-1][1]:
        grp+=1
    else: continue
print(grp) 