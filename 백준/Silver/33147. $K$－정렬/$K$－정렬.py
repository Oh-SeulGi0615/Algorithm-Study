import sys
from math import gcd

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
sorted_arr = sorted(arr)

g = gcd(n, k)
result = 'YES'
for i in range(0, g-1):
  set_arr = set([arr[j] for j in range(0, n, g)])
  set_sorted_arr = set([sorted_arr[j] for j in range(0, n, g)])

  if set_arr != set_sorted_arr:
    result = 'NO'

print(result)