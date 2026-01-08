import sys
input = sys.stdin.readline

n, t = map(int, input().split())

arr = [0 for _ in range(1001)]
min_s, max_e = 10**9, 0

for _ in range(n):
  k = int(input())
  for _ in range(k):
    s, e = map(int, input().split())

    if s < min_s:
      min_s = s
    if e > max_e:
      max_e = e

    for i in range(s+1, e+1):
      arr[i] += 1

res = 0
res_x = 0
for x in range(min_s, max_e-t+2):
  if sum(arr[x:x+t]) > res:
    res = sum(arr[x:x+t])
    res_x = x-1

print(res_x, res_x+t)