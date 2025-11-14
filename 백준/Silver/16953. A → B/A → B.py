import sys

a, b = map(int, sys.stdin.readline().split())

cnt = 1
find = False
result = b
while result > 0:
  if result == a:
    find = True
    break

  if result % 2 == 0:
    result //= 2
    cnt += 1
  elif result % 10 == 1:
    if len(str(result)) > 1:
      result //= 10
      cnt += 1
    else:
      result = 0
      cnt += 1
  else:
    break

if find == True:
  print(cnt)
else:
  print(-1)