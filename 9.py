a = input().split("+")
b = sorted(a)
for i in range(len(a)):
    if i == len(a)-1:
        print(str(b[i])); break
    else: print(str(b[i]),end = "+")