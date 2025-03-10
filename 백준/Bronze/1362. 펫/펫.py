n = 1
while True:
    r = []
    o, w = map(int, input().split())
    if w <= 0:
        status = 'RIP'
        r.append(status)
    elif 0 < w <= o/2:
        status = ':-('
        r.append(status)
    elif o/2 < w < 2*o:
        status = ':-)'
        r.append(status)

    if o == 0 and w == 0:
        break
    else:
        while True:
            a, b = input().split()
            if a == '#' and b == '0':
                break

            elif a == 'F':
                w += int(b)
            elif a == 'E':
                w -= int(b)

            if w <= 0:
                status = 'RIP'
                r.append(status)
            elif o/2 < w < 2*o:
                status = ':-)'
                r.append(status)
            else:
                status = ':-('
                r.append(status)
    if 'RIP' in r:
        print(n, 'RIP')
    else:
        print(n, r[-1])
    n += 1