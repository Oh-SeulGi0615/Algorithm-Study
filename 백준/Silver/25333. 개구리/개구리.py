import sys
input = sys.stdin.readline
from math import gcd

n = int(input())

for _ in range(n):
    a, b, x = map(int, input().split())

    t = gcd(a, b)

    if t > 1:
        print(x // t)
    else:
        print(x)