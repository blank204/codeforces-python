for _ in range(int(input())):
    a,b = map(int, input().split())
    i = 0

    while a<=b:
        a+=i
        i+=1

    print(i-1)

