for t in range(int(input())):

    s = input()
    T = ''

    n0 , n1 = 0,0
    for i in s:
        if i == '0':
            n0 += 1
        else:
            n1 += 1

    check = False
    for i in s:

        if i == '0':
            if n1 == 0:
                check = True
                break
            n1 -= 1
            T += '1'

        else:
            if n0 == 0:
                check = True
                break
            n0 -= 1
            T += '0'

        if check:
            break

    x = n1+n0
    if n0 == 0:
        for i in range(len(s) - n0 - n1, len(s)):
            if s[i] == '1':
                break
            x -= 1
    else:
        for i in range(len(s) - n0 - n1, len(s)):
            if s[i] == '0':
                break
            x -= 1

    print(x)