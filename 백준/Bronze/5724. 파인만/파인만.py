import sys
input = sys.stdin.readline
import math

while True:
    n = int(input())
    if n == 0:
        break

    arr = [i**2 for i in range(1,n+1)]
    print(sum(arr))