t = int(input())

while t:
    t-=1

    a,b = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    temp = 1
    temp2 = temp

    for i in range(1,len(arr)):
        if(arr[i] - arr[i-1]) > b:
            temp = 1
        
        else:
            temp += 1
        temp2 = max(temp,temp2)
    
    print(len(arr)-temp2)