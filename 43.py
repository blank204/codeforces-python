a = int(input())
count = 0

while a:
    if a >= 100:
        count += a//100
        a%=100
    elif a >= 20:
        count += a//20
        a%=20
    elif a >= 10:
        count += a//10
        a%=10
    elif a >= 5:
        count += a//5
        a%=5
    else:
        count += a
        a = 0

print(count)