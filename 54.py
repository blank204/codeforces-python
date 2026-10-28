n = int(input())
a = list(map(int, input().split(" ")))
cops = 0
crime = 0

for i in range(len(a)):
    if a[i] == -1:
        if cops == 0:
            crime+=1
        else:
            cops -=1
    else:
        cops+=a[i]

print(crime)