import sys

n = int(sys.stdin.readline())
m, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

p = m * k
arr = sorted(arr)[::-1]
if p > sum(arr):
  print('STRESS')
else:
  cnt = 0
  for pen in arr:
    if p > 0:
      cnt += 1
      p -= pen
  print(cnt)