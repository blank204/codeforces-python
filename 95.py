n = int(input())
b = ''

while n:
    b += str(n%2)
    n//=2

print(b.count('1'))