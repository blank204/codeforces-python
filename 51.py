def solve(b):
    string = str(b)
    length = len(string)
    arr = list()
    
    for i in range(len(string)):
        if string[i] != '0':
            arr.append(string[i]+'0'*(length-1))
        length-=1
    
    print(len(arr))
    print(*arr)

n = int(input())

while n:
    b = int(input())
    solve(b)
    n-=1
