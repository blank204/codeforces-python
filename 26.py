a , b = map(int, input().split(" "))
c = input()
d = list('A'*len(c))

while b:
    if "BG" in str(c):
        c = c.replace("BG","GB")
    b-=1

print(c)