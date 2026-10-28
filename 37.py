n = int(input())
str = ""

for i in range(n):
    if i == 0: str+="I hate "; continue
    if i%2==1: str+="that I love "; continue
    if i%2==0: str+="that I hate "; continue
print(str+"it")