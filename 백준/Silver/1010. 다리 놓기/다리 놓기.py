import sys
input = sys.stdin.readline
import math

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())

    result = math.comb(b, a)

    print(result)