import sys
input = sys.stdin.readline

from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(1, n+1):
  sub = combinations(arr, i)

  for comp in list(sub):
    if sum(comp) == s:
      cnt += 1

print(cnt)