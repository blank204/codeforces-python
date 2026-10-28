def nexti(a) -> int:
    while True:
        a+=1
        b = str(a)
        if len(list(b)) == len(set(b)):
            return a
        else:
            continue

a = int(input())
print(nexti(a))