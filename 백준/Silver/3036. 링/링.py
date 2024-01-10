import sys
input = sys.stdin.readline

from math import gcd

n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    gcd_ = gcd(arr[0], arr[i])
    print(f'{int(arr[0] / gcd_)}/{int(arr[i] / gcd_)}')