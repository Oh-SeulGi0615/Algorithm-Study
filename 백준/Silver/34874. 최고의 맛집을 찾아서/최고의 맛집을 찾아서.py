import sys
input = sys.stdin.readline

n, m = map(int, input().split())

score = [0 for _ in range(m)]
for _ in range(n):
  arr = list(map(int, input().split()))
  best = max(arr)

  for i in range(m):
    if arr[i] != best:
      score[i] += 1

print(*score)