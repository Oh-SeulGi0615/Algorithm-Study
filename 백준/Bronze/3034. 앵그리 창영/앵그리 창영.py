import sys
input = sys.stdin.readline
import math

n, h, w = map(int, input().split())

length = int(math.sqrt((h**2 + w**2)))
for i in range(n):
    a = int(input())
    if a <= length:
        print('DA')
    else:
        print('NE')