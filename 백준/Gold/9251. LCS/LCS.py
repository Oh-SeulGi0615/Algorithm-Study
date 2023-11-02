import sys
input = sys.stdin.readline

from itertools import combinations

string1 = input().rstrip()
string2 = input().rstrip()

h, w = len(string1), len(string2)
dp = [[0] * (w+1) for _ in range(h+1)]

for i in range(1, h+1):
    for j in range(1, w+1):
        if string1[i-1] == string2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])