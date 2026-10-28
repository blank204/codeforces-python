n = int(input())
d = dict()

while n:
    n-=1 
    a = input()

    d[a] = d.get(a,0) + 1

m1 = 0
m2 = ''

for i in d.items():
    if i[1] > m1:
        m1 = i[1]
        m2 = i[0]

print(m2)