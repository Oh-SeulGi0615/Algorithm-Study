import sys
input = sys.stdin.readline

h, w, n, m = map(int, input().split())

a, b = 0, 0
for i in range(1, h+1, 1+n):
    a += 1
for j in range(1, w+1, 1+m):
    b += 1

print(a*b)