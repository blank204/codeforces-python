n = int(input())
a = []

for i in range(n):
    a.append(input())

for i in a:
    if len(i) > 10: print(i[0] + str(len(i)-2) + i[len(i)-1])
    else: print(i)
