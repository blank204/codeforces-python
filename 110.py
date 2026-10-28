s = 0

for i in range(1,631000):
    a = i**2

    if a%2!=0:
        s+=a

print(s)