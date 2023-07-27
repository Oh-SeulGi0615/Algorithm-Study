import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

x = a * p

if p <= c:
    y = b
else:
    y = b + (d * (p - c))

print(min(x, y))