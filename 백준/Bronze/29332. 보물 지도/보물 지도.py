import sys
input = sys.stdin.readline

n = int(input())
l_, r_, u_, d_ = None, None, None, None
for _ in range(n):
  x, y, d = input().rstrip().split()

  if d == 'L':
    res = int(x) - 1
    if r_ == None or r_ > res:
      r_ = res
  elif d == 'R':
    res = int(x) + 1
    if l_ == None or l_ < res:
      l_ = res
  elif d == 'U':
    res = int(y) + 1
    if d_ == None or d_ < res:
      d_ = res
  elif d == 'D':
    res = int(y) - 1
    if u_ == None or u_ > res:
      u_ = res

if None in [l_, r_, u_, d_]:
  print('Infinity')
else:
  res = (abs(l_ - r_) + 1) * (abs(u_ - d_) + 1)
  print(res)