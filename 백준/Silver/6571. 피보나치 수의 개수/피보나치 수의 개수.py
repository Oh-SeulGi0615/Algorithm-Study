import sys
input = sys.stdin.readline

f = [1, 2]
while True:
  if f[-1] > 10**100:
    break
  result = f[-1] + f[-2]
  f.append(result)

while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    break

  cnt = 0
  for comp in f:
    if a <= comp <= b:
      cnt += 1
  print(cnt)