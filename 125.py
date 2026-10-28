from sys import stdin
input = stdin.readline

for t in range(int(input())):
    n = int(input())

    check = True
    while check:
        N = n
        while N:
            i = N%10
            N //= 10
            if i != 0 and n % i != 0:
                n += 1
                break
        else:
            check = False

    print(n)