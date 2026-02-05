import sys
input = sys.stdin.readline

import math

n, m, k = map(int, input().split())

res = 1
for i in range(k):
  res -= (math.comb((n-m), m-i) * math.comb(m, i)) / math.comb(n, m)

print(res)