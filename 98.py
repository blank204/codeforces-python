n = int(input())
a = list(map(int, input().split()))
n1 = int(input())

while n1:
    n1-=1
    a1 = int(input())
    s = 0

    for i in a:
        if a1 >= i:
            s+=1
    
    print(s)
    