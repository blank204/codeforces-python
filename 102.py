import math
n = int(input())

while n:
    n-=1    
    a,b = map(int, input().split())
    print(int(math.ceil(abs((b-a))/10)))
