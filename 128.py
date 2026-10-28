for _ in range(int(input())):
    n = int(input())
    result = []
    
    for i in range(n):
        result.extend([i+1,n+2*i+1,n+2*i+2])
    print(*result)