for _ in range(int(input())):
    n = sorted(list(map(int, input().split())))

    print(-1*sum(n[:-1]) + n[-1])