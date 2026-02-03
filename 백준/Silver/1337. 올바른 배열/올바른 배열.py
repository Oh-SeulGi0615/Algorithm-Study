import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr = sorted(arr)

best = 1
for i in range(n-1):
  for j in range(n-1, i, -1):
    if arr[j] - arr[i] <= 4 and len(arr[i:j+1]) > best:
      best = len(arr[i:j+1])
print(5 - best)