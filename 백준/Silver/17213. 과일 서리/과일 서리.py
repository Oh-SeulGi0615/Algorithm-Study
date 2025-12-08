import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dp = [[0 for _ in range(m)] for _ in range(n)] 
dp[0] = [1] * m

for i in range(1, n):
  for j in range(1, m):
    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
  
print(dp[-1][-1])