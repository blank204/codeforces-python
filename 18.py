def islucky(a,count):
    for i in a:
        if i == '4' or i == '7': 
            count+=1            
        else: continue
    return count

a = input()
b = islucky(a,0)

if b == 4 or b == 7:
    print("YES")
else:
    print("NO")