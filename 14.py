a = int(input())
count = 0

if a >= 5:
    count+=a//5
    a%=5
if a: count+=1
print(count)
