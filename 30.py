n = int(input())
count = 0

while n:
    b,c = map(int,input().split(" "))
    if (c-b) >= 2:
        count+=1
    n-=1
print(count)