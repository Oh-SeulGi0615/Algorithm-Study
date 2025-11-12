import sys

n, x = map(int, sys.stdin.readline().split())
total = sum(list(map(int, sys.stdin.readline().split())))

if total % x == 0:
  print(1)
else:
  print(0)