import sys

f, c, e, b = map(int, sys.stdin.readline().split())
f_, c_, e_, b_ = map(int, sys.stdin.readline().split())

cookies = 0
for _ in range(int(sys.stdin.readline())):
    q1, q2 = map(int, sys.stdin.readline().split())

    if q1 == 1:
        if (f - (f_ * q2) >= 0) and (c - (c_ * q2) >= 0) and (e - (e_ * q2) >= 0) and (b - (b_ * q2) >= 0):
            cookies += q2
            f -= f_ * q2
            c -= c_ * q2
            e -= e_ * q2
            b -= b_ * q2
            print(cookies)
        else:
            print('Hello, siumii')
    elif q1 == 2:
        f += q2
        print(f)
    elif q1 == 3:
        c += q2
        print(c)
    elif q1 == 4:
        e += q2
        print(e)
    else:
        b += q2
        print(b)