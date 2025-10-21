import sys

n, q = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

list_sum = [0]
now = 0
for i in range(1, n):
  now += abs(arr[i] - arr[i-1])
  list_sum.append(now)

for _ in range(q):
  s, e = map(int, sys.stdin.readline().split())
  print(list_sum[e-1] - list_sum[s-1])