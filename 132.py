import math

t = int(input())

def solve():
    for i in a:
        for j in a:
            if math.gcd(i,j) <= 2:
                return 'YES'
    
    return 'NO'


while t:
    t-=1
    n = int(input())
    a = list(map(int, input().split()))

    print(solve())
