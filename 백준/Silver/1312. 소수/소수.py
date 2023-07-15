import sys
input = sys.stdin.readline

a, b, n = map(int, input().split())

i = 1
c = a // b
d = a % b
while i <= n:
     c = (d * 10) // b
     d = (d * 10) % b
     i += 1

print(c)