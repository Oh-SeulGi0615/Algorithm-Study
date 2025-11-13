import sys

n = int(sys.stdin.readline())

cnt = 0
while n > 0:
  if '1' not in str(n):
    n -= 1
    cnt += 1
  elif len(str(n)) > 1:
    n = int(str(n).replace('1', '', 1))
    cnt += 1
  else:
    n = 0
    cnt += 1

print(cnt)