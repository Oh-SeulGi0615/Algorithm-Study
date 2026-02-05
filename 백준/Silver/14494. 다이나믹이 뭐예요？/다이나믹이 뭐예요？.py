import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dp = [[1 if i == 0 or j == 0 else 0 for i in range(m)] for j in range(n)]
for a in range(1, n):
  for b in range(1, m):
    dp[a][b] = (dp[a-1][b] + dp[a][b-1] + dp[a-1][b-1]) % 1000000007

print(dp[-1][-1])