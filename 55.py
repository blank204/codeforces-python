n , a = map(int, input().split(" "))
count = 0
summ = 0

for i in range(1,n+1):
    summ+=5*i
    if summ + a >= 240:
        print(count if summ+a!=240 else count+1)
        quit()
    count+=1
print(count)