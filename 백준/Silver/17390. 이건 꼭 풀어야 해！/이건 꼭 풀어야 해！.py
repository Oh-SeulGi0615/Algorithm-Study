import sys

n, q = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))

sum = [arr[0]]
for i in range(1, len(arr)):
  sum.append(sum[-1] + arr[i])

for _ in range(q):
  l, r = map(int, sys.stdin.readline().split())

  if l == 1:
    print(sum[r-1])
  else:
    print(sum[r-1] - sum[l-2])