n = int(input())

if n == 1:
    print(1)
    quit()
else:
    print(n, end = ' ')

while True:
    if n == 1:
        break
    
    elif n % 2 == 0:
        n = n//2 
        print(n,end = ' ')
    
    elif n % 2 != 0:
        n = n*3 + 1
        print(n, end = ' ')
    