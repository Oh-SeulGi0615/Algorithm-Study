import sys

n = int(sys.stdin.readline())
min_, max_ = 0, 0

for _ in range(n):
  a, b = map(int, sys.stdin.readline().split())
  if min_ < min(a, b):
    min_ = min(a, b)
  if max_ < max(a, b):
    max_ = max(a, b)

print(min_ * max_)