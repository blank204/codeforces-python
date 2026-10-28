a,b,c = map(int, input().split(" "))
sum = 0

sum = int((c/2)*(2*a + (c-1)*a))

print((sum-b) if (sum-b)>0 else 0)
