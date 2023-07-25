import sys
input = sys.stdin.readline
import math

n = int(input())

arr = [math.factorial(i) for i in range(21)]

cnt = 0
for i in range(len(arr)-1, -1, -1):
    if arr[i] <= n:
        n -= arr[i]
        cnt += 1

if n == 0 and cnt > 0:
    print('YES')
else:
    print('NO')