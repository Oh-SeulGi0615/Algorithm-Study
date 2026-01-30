import sys
input = sys.stdin.readline

n = input().rstrip()
list_n = list(map(int, n))

if '0' not in n:
  print(-1)
elif sum(list_n) % 3 != 0:
  print(-1)
else:
  list_n = sorted(list_n, key=lambda x: -x)
  res = ''.join(list(map(str, list_n)))
  print(res)