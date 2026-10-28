b = input()
a = b[1:-1:1].split(', ') 

print(len(set(a)) if b!="{}" else 0)
