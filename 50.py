n1 = input()
n2 = input()
n3 = input()
a = [0]*26
b = [0]*26

for i in n1:
    a[ord(i)-65]+=1

for i in n2:
    a[ord(i)-65]+=1

for i in n3:
    b[ord(i)-65]+=1

print("YES" if a==b else "NO")

