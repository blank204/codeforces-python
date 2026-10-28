# n,m = map(int, input().split())
# a = list(map(int, input().split()))
# s = 0
# cp = 1

# for i in a:
#     if i < cp:
#         s += (n-cp) + i
#         cp = i
#     else:
#         s += (i-cp)
#         cp = i
        
# print(s)

'''
Write a program to get a list which consist of tuples having 2 elements and display the sorted list in ascending order by the last element in each tuple.
Ex: [(2,5), (3,7), (2,3)]
[(2,3), (2,5), (3,7)]
'''
a = [(2,5), (3,7), (2,3)]
k = 0

for i in range(len(a)):
    minn = a[k][1]
    mine = 0
    for j in range(k,len(a)):
        if minn >= a[j][1]:
            minn = a[j][1]
            mine = a[j]
    a.remove(mine)
    a.insert(k,mine)
    k += 1

print(a)

