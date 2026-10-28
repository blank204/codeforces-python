def finding(x, count):
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            count+=1
    return count

a = int(input())
b = input()

print(finding(b,0))