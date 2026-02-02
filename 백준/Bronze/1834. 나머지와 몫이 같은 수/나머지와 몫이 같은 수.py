import sys
input = sys.stdin.readline

n = int(input())

res = 0
for i in range(1, n):
  num = i * n + i
  res += num

print(res)