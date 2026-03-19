import sys
input = sys.stdin.readline

while True:
  g, t, a, d = map(int, input().split())
  if g == -1:
    break

  l = ((t * (t - 1)) // 2) * g
  t_cnt = g * a + d
  res = 0

  for i in range(1, 50):
    if t_cnt == 2**i:
      l += 2**i - 1
    elif 2**(i-1) < t_cnt < 2**i:
      l += 2**i - 1
      res += 2**i - t_cnt

  print(f'{g}*{a}/{t}+{d}={l}+{res}')