dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12]

n = int(input())
for _ in range(n):
    num = int(input())

    if num >= len(dp):
        for i in range(len(dp), num+1):
            dp.append(dp[i-1]+dp[i-5])
    print(dp[num])