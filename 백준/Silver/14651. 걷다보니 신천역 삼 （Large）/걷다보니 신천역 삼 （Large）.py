import sys
input = sys.stdin.readline

n = int(input())

dp = [[-1 for _ in range(3)] for _ in range(n+1)]
dp[1][0] = 0
dp[1][1] = 1
dp[1][2] = 1

for i in range(2, n+1):
  dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % (10**9 + 9)
  dp[i][1] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % (10**9 + 9)
  dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % (10**9 + 9)

print(dp[-1][0])