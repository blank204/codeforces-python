limit = 200000
is_prime = [True] * limit
is_prime[0] = is_prime[1] = False

for i in range(2, int(limit**0.5) + 1):
    if is_prime[i]:    
        for j in range(i*i, limit, i): 
            is_prime[j] = False

primes = []
for i in range(limit):
    if is_prime[i]:
        primes.append(i)

for _ in range(int(input())):
    n = int(input())
    print(*[primes[i] * primes[i+1] for i in range(n)])