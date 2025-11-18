import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * i for i in range(1, n)] + [arr[-1]]

for i in range(n-2, -1, -1):
  for j in range(len(arr[i])):
    for k in range(j, j+2):
      if arr[i][j] + dp[i+1][k] > dp[i][j]:
        dp[i][j] = arr[i][j] + dp[i+1][k]

print(*dp[0])