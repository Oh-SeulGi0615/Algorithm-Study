import sys
input = sys.stdin.readline

from math import gcd

x, y = map(int, input().split())

gcd_ = gcd(x, y)
res = gcd_ * (x // gcd_) * (y // gcd_)
res_x = res // x
res_y = res // y

arr = []
for i in range(1, res+1):
  if i % res_x == 0 and i % res_y == 0:
    arr.append(3)
  elif i % res_x == 0:
    arr.append(1)
  elif i % res_y == 0:
    arr.append(2)

print(*arr, sep='')