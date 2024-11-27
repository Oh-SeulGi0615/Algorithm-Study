import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0 for _ in range(n)]
for i in range(n):
  if i == 0:
    prefix_sum[0] = arr[0]
  else:
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

for _ in range(m):
  i, j = map(int, sys.stdin.readline().split())
  if i == 1:
    print(prefix_sum[j-1])
  elif i > 1:
    print(prefix_sum[j-1] - prefix_sum[i-2])