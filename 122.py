from sys import stdin
from math import pow
input = stdin.readline
 
for t in range(int(input())):
 
    a,b = map(int,input().split())
 
    check = False
    for i in range(1,31):
 
        for x in range(i):
            if a < pow(b+x,i-x):
                check = True
                break
 
        if check:
            print(i)
            break