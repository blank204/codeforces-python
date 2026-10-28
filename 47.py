n = int(input())
arr = []
arr1 = []
ans = 0

for _ in range(n): 
    j,k = map(int, input().split(" "))
    arr.append(j)
    arr1.append(k)

for i in range(n):
    ans += arr1.count(arr[i]) 
print(ans)
