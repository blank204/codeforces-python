a,b = map(int, input().split(' '))
c = list(map(int, input().split(' ')))
wid = 0

for i in c:
    if i>b: wid+=2
    else: wid+=1
print(wid)