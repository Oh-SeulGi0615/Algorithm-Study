import sys
input = sys.stdin.readline

d1, d2, d3 = map(int, input().split())
d4 = d1 + d2 + d3
a, b, c = 0, 0, 0

a = (d4 / 2) - d3
b = (d4 / 2) - d2
c = (d4 / 2) - d1

if a > 0 and b > 0 and c > 0:
    print(1)
    print(a, b, c)
else:
    print(-1)