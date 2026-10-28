# a = input()
# m = 0
# curr = a[0]
# tc = 0

# for i in a:
#     if i == curr:
#         tc += 1
#     else:
#         m = max(m,tc)
#         tc = 1
#         curr = i

# m = max(m,tc)
# print(m)

a = input()
i,j = 0,0
m = 0

while j < len(a) - 1:   
    if a[j] != a[j+1]:
        m = m if m>(j-i+1) else j-i+1
        i,j = j+1,j+1
        continue
    j += 1


if a[j] == a[j-1]:
    m = m if m>(j-i+1) else j-i+1

print(m)