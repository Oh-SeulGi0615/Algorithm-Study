import sys
input = sys.stdin.readline

w, l, d = map(float, input().split())

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
dp[0][0][0] = 1.0

tier = [0, 0, 0, 0, 0]
for i in range(21):
  for j in range(21):
    for k in range(21):
      if i+j+k < 20:
        dp[i][j][k+1] += dp[i][j][k] * w
        dp[i][j+1][k] += dp[i][j][k] * l
        dp[i+1][j][k] += dp[i][j][k] * d
      
      if i+j+k == 20:
        score = 2000 + 50 * (k - j)
        if score < 1500:
          tier[0] += dp[i][j][k]
        elif score < 2000:
          tier[1] += dp[i][j][k]
        elif score < 2500:
          tier[2] += dp[i][j][k]
        elif score < 3000:
          tier[3] += dp[i][j][k]
        else:
          tier[4] += dp[i][j][k]

tier = list(map(lambda x: f'{x:.8f}', tier))
print(*tier, sep='\n')