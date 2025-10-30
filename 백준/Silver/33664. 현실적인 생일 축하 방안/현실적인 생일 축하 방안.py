import sys

b, n, m = map(int, sys.stdin.readline().rstrip().split())

items = {}
for _ in range(n):
  i, p = sys.stdin.readline().rstrip().split()
  items[i] = int(p)

result = 0
for _ in range(m):
  j = sys.stdin.readline().rstrip()
  result += items[j]

if result > b:
  print('unacceptable')
else:
  print('acceptable')