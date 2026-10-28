n = int(input())
a = []
count = 0

for i in range(n):
    a.append(input())

for i in a:
    if i.count('1') >= 2:
        count+=1
print(count)

