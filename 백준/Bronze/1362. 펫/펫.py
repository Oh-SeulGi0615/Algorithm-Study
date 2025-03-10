n = 1
while True:
    status = ''
    o, w = map(int, input().split())

    if w <= 0:
        status = 'RIP'

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
            elif status != 'RIP' and o/2 < w < 2*o:
                status = ':-)'
            elif status != 'RIP' and (w >= 2*o or w <= o/2):
                status = ':-('
    
    print(n, status)
    n += 1