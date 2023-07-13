import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())

if r % n > 0:
    a = (r // n) + 1
else:
    a = r // n

if c % n > 0:
    b = (c // n) + 1
else:
    b = c // n

print(a*b)