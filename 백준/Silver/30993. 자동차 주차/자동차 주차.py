import sys
input = sys.stdin.readline

import math

k, a, b, c = map(int, input().split())

result = math.comb(k, a) * math.comb(k-a, b)
print(result)