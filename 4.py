n = int(input())
a = []
count = 0

for i in range(n):
    a.append(input())

for i in a:
    if '++' in i:
        count+=1
    elif '--' in i:
        count-=1
print(count)

