import sys
input = sys.stdin.readline

from itertools import combinations

n, m, k = map(int, input().split())
combs = list(combinations([i for i in range(1, (2*n)+1)], n))

arr = []
for _ in range(m):
  sub = set(map(int, input().split()))
  arr.append(sub)

best = 0
for i in combs:
  cnt = 0
  comb = set(i)
  for case in arr:
    if case <= comb:
      cnt += 1
  if cnt > best:
    best = cnt

print(best)