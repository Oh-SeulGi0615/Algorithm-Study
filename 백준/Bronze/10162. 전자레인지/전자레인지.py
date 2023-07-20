import sys
input = sys.stdin.readline

t = int(input())

a, b, c = 300, 60, 10

x, d = divmod(t, a)
y, e = divmod(d, b)
z, f = divmod(e, c)

if f > 0:
    print(-1)
else:
    print(x, y, z)