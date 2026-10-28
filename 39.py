n = int(input())
str = input()

if n<26:
    print("NO")
else: 
    if len(set(str.lower())) != 26:
        print("NO")
    else:
        print("YES")