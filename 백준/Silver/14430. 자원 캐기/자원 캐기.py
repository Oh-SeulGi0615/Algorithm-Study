import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1e9] * m for _ in range(n)]

for i in range(n):
  for j in range(m):
    if i == 0 and j == 0:
      dp[0][0] = arr[0][0]
    elif i == 0:
      dp[0][j] = dp[0][j-1] + arr[0][j]
    elif j == 0:
      dp[i][0] = dp[i-1][0] + arr[i][0]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + arr[i][j]

print(dp[-1][-1])