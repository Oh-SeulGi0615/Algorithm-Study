import sys
input = sys.stdin.readline

a, b = map(int, input().split())

if a >= 4 and a % 2 != 0:
  a += 1

res = 0
for i in range(max(4, a), b+1, 2):
  res += i

print(res)