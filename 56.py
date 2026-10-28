n = int(input())
a = list(map(int, input().split(" ")))
maxx = minn = a[0]
amaze = 0

for i in range(1,len(a)):
    if a[i] > maxx:
        maxx = a[i]
        amaze += 1
    elif a[i] < minn:
        minn = a[i]
        amaze+=1

print(amaze)