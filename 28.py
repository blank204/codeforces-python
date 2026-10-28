'''
You are given an array a of n numbers. 
You have to perform k operations:
Given 2 numbers l and r: for all i such that 1 <= i <= n: if l<=ai<=r :ai=ai+1
Output the maximum element in the array after the k operations.

Input:
t test cases
n k
This row contains n elements representing array a
followed by k rows containing 2 numbers: l r

Output: single number for each test case (the maximum element in the array)
'''

def somefunction(k,a,l):
    temp = 0
    m = max(a)
    while temp < k:
        if l[temp][0]<= m <= l[temp][1]:
            m+=1
        temp+=1
    return m      

t  = int(input())

for _ in range(t):
    n , k = map(int, input().split())
    a = list(map(int, input().split(" ")))
    l = list()
    for __ in range(k):
        l.append(tuple(map(int, input().split())))
    print(somefunction(k,a,l))


'''
1
5 3
1 2 3 2 1
1 2
2 3
1 3


 # for i in range(len(a)):
    #     if temp == k: break
    #     if l[temp][0]<= a[i] <= l[temp][1]:
    #         a[i]+=1
    #     temp+=1
'''