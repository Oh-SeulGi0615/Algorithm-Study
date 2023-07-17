import sys
input = sys.stdin.readline

n = int(input())
p = int(input())

if 5 <= n < 10:
    p -= 500
elif 10 <= n < 15:
    if int(0.1 * p) > 500:
        p = int(0.9 * p)
    else:
        p -= 500
elif 15 <= n < 20:
    if int(0.1 * p) > 2000:
        p = int(0.9 * p)
    else:
        p -= 2000
elif 20 <= n:
    if int(0.25 * p) > 2000:
        p = int(0.75 * p)
    else:
        p -= 2000

if p < 0:
    print(0)
else:
    print(p)