import sys
input = sys.stdin.readline
import math

n = int(input())
arr = list(map(int, input().split()))[::-1]

a, b = 1, 1
for i in range(n):
    if i == 0:
        b = arr[0]
    else:
        a = b * arr[i] + a
        a, b = b, a
a = b - a

c = math.gcd(a, b)
print(int(a / c), int(b / c))