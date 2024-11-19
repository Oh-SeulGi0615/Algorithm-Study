dp = [0, 1, 1, 1]
num = 4

while num < 117:
    new = dp[num-1] + dp[num-3]
    dp.append(new)
    num += 1

n = int(input())
print(dp[n])