a = input()
count = 0

for i in a:
    if i.isupper():
        count+=1

if count <= (len(a)-count):print(a.lower())
else: print(a.upper())
