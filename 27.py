def beauty(n,k,b,s):
    aux = list()
    aux.append(b*k)    
    s-=aux[0]
    limit = k-1
    
    while len(aux) < n and s>0:
        t = min(k-1,s)
        aux.append(t)
        s-=t
    
    while len(aux) != n:
        aux.append(0)

    if s > max(0,limit) or s < 0: return -1
    else: 
        aux[0] = aux[0] + s if s>0 else aux[0]
        return " ".join(map(str,aux))


a = int(input())

for _ in range(a):
    n,k,b,s = map(int, input().split(' '))
    print(beauty(n,k,b,s))

