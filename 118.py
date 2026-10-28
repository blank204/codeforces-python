n = int(input())

while n:
    n-=1
    n1 = int(input())
    a = sorted(list(map(int, input().split())))

    if len(a) == 1:
        print("YES")
    else:
        for i in range(1,len(a)):
            if a[i] - a[i-1] > 1:
                print("NO")
                break
        else:
            print("YES")