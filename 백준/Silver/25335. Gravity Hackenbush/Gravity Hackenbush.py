import sys
n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
  x, y = map(int, sys.stdin.readline().split())
  arr.append([x, y])

r, g, b = 0, 0, 0
for _ in range(m):
  v, w, c = sys.stdin.readline().split()
  if c == 'R': r += 1
  elif c == 'G': g += 1
  else: b += 1

p1, p2 = 0, 0
if g % 2 == 0:
  p1 = r + (g // 2)
  p2 = b + (g // 2)
else:
  p1 = r + (g // 2) + 1
  p2 = b + (g // 2)

if p1 > p2:
  print('jhnah917')
else:
  print('jhnan917')