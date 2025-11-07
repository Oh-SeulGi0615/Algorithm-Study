import sys

a, b = map(int, sys.stdin.readline().split())

if a == 1 and b == 1:
  print(3600 * 24)
else:
  diff = abs(1 - (a / b))
  print(int(2 * diff))