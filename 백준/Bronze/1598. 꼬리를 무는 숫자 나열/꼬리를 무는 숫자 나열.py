import sys
input = sys.stdin.readline

a, b = map(int, input().split())

c, d = divmod(a, 4)
e, f = divmod(b, 4)

if d == 0:
    x1 = c
    y1 = 4
elif 0 < d < 4:
    x1 = c + 1
    y1 = d

if f == 0:
    x2 = e
    y2 = 4
elif 0 < f < 4:
    x2 = e + 1
    y2 = f

print(abs(x2 - x1) + abs(y2 - y1))